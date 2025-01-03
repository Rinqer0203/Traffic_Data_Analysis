'''
LABELの相関係数ヒートマップを生成するスクリプト
'''
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os
from utils.tsv_header_adder import get_tsv_with_header
from utils.traffic_attributes import TrafficAttr

DATA_PATH = './data/20150120.txt'
OUTPUT_DIR = './output/correlation_heatmap'


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    data = pd.read_csv(get_tsv_with_header(DATA_PATH), delimiter='\t')

    # 相関を調べる属性のリスト
    selected_columns = [
        TrafficAttr.DURATION.name,
        TrafficAttr.SOURCE_BYTES.name,
        TrafficAttr.DESTINATION_BYTES.name,
        TrafficAttr.COUNT.name,
        TrafficAttr.SAME_SRV_RATE.name,
        TrafficAttr.SERROR_RATE.name,
        TrafficAttr.SRV_SERROR_RATE.name,
        TrafficAttr.DST_HOST_COUNT.name,
        TrafficAttr.DST_HOST_SRV_COUNT.name,
        TrafficAttr.DST_HOST_SAME_SRC_PORT_RATE.name,
        TrafficAttr.DST_HOST_SERROR_RATE.name,
        TrafficAttr.DST_HOST_SRV_SERROR_RATE.name,
        TrafficAttr.SOURCE_PORT_NUMBER.name,
        TrafficAttr.LABEL.name
    ]

    # 選択した列だけを取り出す
    selected_data = data[selected_columns]

    # 3種類の相関方法を計算し、それぞれ保存
    correlation_methods = ['pearson', 'spearman', 'kendall']
    for method in correlation_methods:
        # 相関行列の計算
        correlation_matrix = selected_data.corr(method=method)

        # ヒートマップ作成
        plt.figure(figsize=(14, 14))
        sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)
        plt.title(f"Correlation Matrix ({method.capitalize()})", fontsize=16)
        plt.tight_layout()

        # 画像保存
        output_img_path = f'{OUTPUT_DIR}/correlation_matrix_{method}.png'
        plt.savefig(output_img_path)
        print(f'Saved {output_img_path}')
        plt.close()


if __name__ == '__main__':
    main()
