import os
import random
from utils.traffic_attributes import TrafficAttributes

DATA_PATH = './data/20150101.txt'
OUT_PATH = './output/sampled_traffic/sampled.txt'

os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)


def extract_samples_by_label(data_path, label_value, sample_size):
    """指定されたLABELの値に基づいてランダムサンプリングを行う"""
    with open(data_path, 'r') as file:
        lines = [line.strip() for line in file if line.split('\t')[TrafficAttributes.LABEL] == label_value]
    return random.sample(lines, min(len(lines), sample_size))


def main():
    sample_size = 10000

    # 各ラベルごとにサンプリング
    normal_samples = extract_samples_by_label(DATA_PATH, '1', sample_size)  # LABEL = 1 (正常)
    known_attack_samples = extract_samples_by_label(DATA_PATH, '-1', sample_size)  # LABEL = -1 (既知の攻撃)
    unknown_attack_samples = extract_samples_by_label(DATA_PATH, '-2', sample_size)  # LABEL = -2 (未知の攻撃)

    # サンプルを統合
    sampled_data = normal_samples + known_attack_samples + unknown_attack_samples
    random.shuffle(sampled_data)

    # 保存
    with open(OUT_PATH, 'w') as f:
        f.write("\n".join(sampled_data))

    print(f"Saved {len(sampled_data)} samples to {OUT_PATH}.")


if __name__ == '__main__':
    main()
