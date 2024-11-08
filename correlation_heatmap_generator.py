import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os
import tsv_header_adder

DATA_PATH = './data/20150101.txt'
OUTPUT_DIR = './output/correlation_heatmap'
os.makedirs(OUTPUT_DIR, exist_ok=True)

data = pd.read_csv(tsv_header_adder.get_tsv_with_header(DATA_PATH), delimiter='\t')

# 相関を調べる属性のリスト
selected_columns = ['DURATION', 'SOURCE_BYTES', 'DESTINATION_BYTES', 'COUNT', 'SAME_SRV_RATE', 'SERROR_RATE', 'SRV_SERROR_RATE', 'DST_HOST_COUNT',
                    'DST_HOST_SRV_COUNT', 'DST_HOST_SAME_SRC_PORT_RATE', 'DST_HOST_SERROR_RATE', 'DST_HOST_SRV_SERROR_RATE', 'SOURCE_PORT_NUMBER', 'LABEL']

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
    output_img_path = os.path.join(OUTPUT_DIR, f'correlation_matrix_{method}.png')
    plt.savefig(output_img_path)
    plt.close()
