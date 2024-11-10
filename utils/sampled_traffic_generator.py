'''
トラフィックデータからLABELの値に基づいてランダムサンプリングを行うスクリプト
'''
import os
import random
from collections import defaultdict
from utils.traffic_attributes import TrafficAttr

DATA_DIR = './data'
OUT_PATH = './output/sampled_traffic/sampled.txt'
SAMPLED_SIZE = 10000


def get_sampled_data(file_path=None) -> str:
    '''
    各LABELのサンプルを取得し、統合して保存する
    '''
    # サンプリングするデータのファイルパスを決定
    if file_path is None:
        data_files = [os.path.join(DATA_DIR, filename) for filename in os.listdir(DATA_DIR)
                      if os.path.isfile(os.path.join(DATA_DIR, filename))]
    else:
        data_files = [file_path]

    # 各LABELのサンプルを取得
    sampled_data = extract_samples(data_files, SAMPLED_SIZE)

    # サンプルを統合
    all_samples = sampled_data['1'] + sampled_data['-1'] + sampled_data['-2']
    random.shuffle(all_samples)

    # 保存
    os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)
    with open(OUT_PATH, 'w') as f:
        f.write("\n".join(all_samples))
    print(f"Saved {len(all_samples)} samples to {OUT_PATH}.")
    print(f"Normal: {len(sampled_data['1'])} samples.")
    print(f"Known attack: {len(sampled_data['-1'])} samples.")
    print(f"Unknown attack: {len(sampled_data['-2'])} samples.")
    return OUT_PATH


def extract_samples(data_files, sample_size: int) -> dict:
    """各LABELの値に基づいてランダムサンプリングを行う"""
    label_samples = defaultdict(list)
    for file_path in data_files:
        with open(file_path, 'r') as file:
            for line in file:
                label = line.split('\t')[TrafficAttr.LABEL]
                label_samples[label].append(line.strip())

    sampled_data = {
        '1': random.sample(label_samples['1'], min(len(label_samples['1']), sample_size)),
        '-1': random.sample(label_samples['-1'], min(len(label_samples['-1']), sample_size)),
        '-2': random.sample(label_samples['-2'], min(len(label_samples['-2']), sample_size))
    }
    return sampled_data


def main():
    get_sampled_data()


if __name__ == '__main__':
    main()