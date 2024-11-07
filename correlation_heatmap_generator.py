import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os
import tsv_header_adder

DATA_PATH = './data/20150101.txt'
OUTPUT_IMG_PATH = './output/correlation_matrix.png'

data = pd.read_csv(tsv_header_adder.get_tsv_with_header(DATA_PATH), delimiter='\t')

# 相関を調べる属性のリスト
selected_columns = ['DURATION', 'SOURCE_BYTES', 'DESTINATION_BYTES', 'COUNT', 'SAME_SRV_RATE', 'SERROR_RATE', 'SRV_SERROR_RATE', 'DST_HOST_COUNT',
                    'DST_HOST_SRV_COUNT', 'DST_HOST_SAME_SRC_PORT_RATE', 'DST_HOST_SERROR_RATE', 'DST_HOST_SRV_SERROR_RATE', 'SOURCE_PORT_NUMBER', 'LABEL']

# 選択した列だけを取り出して相関を計算
selected_data = data[selected_columns]
correlation_matrix = selected_data.corr()

# ヒートマップ作成
plt.title("Correlation Matrix", fontsize=16)
plt.figure(figsize=(14, 14))
sns.heatmap(correlation_matrix, annot=True,
            cmap='coolwarm', fmt='.2f', linewidths=0.5)

# plt.show()

plt.tight_layout()
os.makedirs(os.path.dirname(OUTPUT_IMG_PATH), exist_ok=True)
plt.savefig(OUTPUT_IMG_PATH)
