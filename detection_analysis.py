import os
from collections import Counter
from utils.traffic_attributes import TrafficAttr


DATA_PATH = './output/sampled_traffic/sampled.txt'
OUT_DIR = './output/detection'
LOG_DIR = './logs/detection'
SEARCH_TARGETS = [
    TrafficAttr.IDS_DETECTION,
    TrafficAttr.MALWARE_DETECTION,
    TrafficAttr.ASHULA_DETECTION
]


def update_counter(line: str, total_counter: Counter, target_counters: list, target_detail_counters: list) -> None:
    items = line.split('\t')
    total_counter['total_traffic'] += 1
    if items[TrafficAttr.LABEL] != '1':
        total_counter['total_attack'] += 1

    for i, target in enumerate(SEARCH_TARGETS):
        if items[target] != '0':
            target_counters[i]['target'] += 1
            target_detail_counters[i][items[target]] += 1
            if items[TrafficAttr.LABEL] != '1':
                target_counters[i]['attack'] += 1


def write_detail_logs(detail_counters: list, detail_files: list) -> None:
    for i, detail_file in enumerate(detail_files):
        detail_file.write('detail\tcount\n')
        for target, count in detail_counters[i].items():
            detail_file.write(f'{target}\t{count}\n')


def write_results(total_counter: Counter, target_counters: list) -> None:
    lines = []
    for item, count in total_counter.items():
        lines.append(f'{item} : {count}\n')
    for i, target in enumerate(SEARCH_TARGETS):
        if (target_counters[i]["target"] == 0):
            attack_rate = 0
        else:
            attack_rate = target_counters[i]["attack"] / target_counters[i]["target"]
        lines.append(f'{target.name}\n')
        lines.append(f'\ttarget : {target_counters[i]["target"]}\n')
        lines.append(f'\tattack : {target_counters[i]["attack"]}\n')
        lines.append(f'\tattack rate : {attack_rate:.2f}\n')
    result_path = f'{OUT_DIR}/result.txt'
    with open(result_path, 'w') as output:
        output.writelines(lines)
    print(''.join(lines))


def main():
    total_counter = Counter()
    target_counters = [Counter() for _ in SEARCH_TARGETS]
    target_detail_counters = [Counter() for _ in SEARCH_TARGETS]

    os.makedirs(LOG_DIR, exist_ok=True)
    os.makedirs(OUT_DIR, exist_ok=True)
    filtered_files = [open(f'{LOG_DIR}/{target.name}_filtered_traffic.txt', 'w') for target in SEARCH_TARGETS]
    details_files = [open(f'{LOG_DIR}/{target.name}_attribute_details.txt', 'w') for target in SEARCH_TARGETS]

    try:
        with open(DATA_PATH, 'r') as input_file:
            for line in input_file:
                update_counter(line, total_counter, target_counters, target_detail_counters)
                # 検出されたトラフィックを対応するログに出力
                for i, target in enumerate(SEARCH_TARGETS):
                    if line.split('\t')[target] != '0':
                        filtered_files[i].write(line)

        write_detail_logs(target_detail_counters, details_files)
        write_results(total_counter, target_counters)

    finally:
        for f in filtered_files + details_files:
            f.close()


if __name__ == '__main__':
    main()
