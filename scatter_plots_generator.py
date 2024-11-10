'''
LABELと他の属性の散布図を生成するスクリプト
'''
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os
from utils.tsv_header_adder import get_tsv_with_header
from utils.traffic_attributes import TrafficAttr


DATA_PATH = './data/20150101.txt'
OUTPUT_DIR = './output/label_scatter_plots'


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    data = pd.read_csv(get_tsv_with_header(DATA_PATH), delimiter='\t')

    # 散布図を作成する属性リスト（LABEL以外の属性）
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
        TrafficAttr.SOURCE_PORT_NUMBER.name
    ]

    # 各属性とLABELの散布図を作成し保存
    for col in selected_columns:
        plt.figure(figsize=(8, 6))
        sns.scatterplot(data=data, x=col, y='LABEL', alpha=0.5)
        plt.title(f'Scatter Plot of {col} vs LABEL')
        plt.xlabel(col)
        plt.ylabel('LABEL')

        # 画像ファイルのパスを指定
        output_file = os.path.join(OUTPUT_DIR, f'scatter_{col}_vs_LABEL.png')
        plt.savefig(output_file)
        print(f'Saved {output_file}')
        plt.close()


if __name__ == '__main__':
    main()
