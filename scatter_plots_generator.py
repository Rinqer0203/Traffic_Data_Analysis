import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os
import tsv_header_adder

DATA_PATH = './data/20150101.txt'
OUTPUT_DIR = './output/label_scatter_plots'
os.makedirs(OUTPUT_DIR, exist_ok=True)

# データを読み込む
data = pd.read_csv(tsv_header_adder.get_tsv_with_header(DATA_PATH), delimiter='\t')

# 散布図を作成する属性リスト（LABEL以外の属性）
selected_columns = [
    'DURATION', 'SOURCE_BYTES', 'DESTINATION_BYTES', 'COUNT', 'SAME_SRV_RATE',
    'SERROR_RATE', 'SRV_SERROR_RATE', 'DST_HOST_COUNT', 'DST_HOST_SRV_COUNT',
    'DST_HOST_SAME_SRC_PORT_RATE', 'DST_HOST_SERROR_RATE', 'DST_HOST_SRV_SERROR_RATE',
    'SOURCE_PORT_NUMBER'
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
    plt.close()
