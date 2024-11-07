from os import makedirs
from typing import NamedTuple
from collections import Counter
from traffic_attributes import TrafficAttributes


class Attribute(NamedTuple):
    index: int
    name: str


DATA_PATH = './data/20150101.txt'
OUT_DIR = './output'
LOG_DIR = './logs'
SEARCH_TARGETS = [Attribute(TrafficAttributes.IDS_DETECTION, 'IDS'),
                  Attribute(TrafficAttributes.MALWARE_DETECTION, 'MALWARE'),
                  Attribute(TrafficAttributes.ASHULA_DETECTION, 'ASHULA')]


def main():
    makedirs(LOG_DIR, exist_ok=True)
    makedirs(OUT_DIR, exist_ok=True)

    # トラフィック全体のカウンタ
    total_counter = Counter()
    # 検索属性ごとのカウンタ
    target_counters = [Counter() for _ in SEARCH_TARGETS]
    # 検索属性ごとの詳細カウンタ
    target_detail_counters = [Counter() for _ in SEARCH_TARGETS]

    filltered_files = []
    details_files = []

    try:
        # すべてのログを開いとく (finnalyでclose)
        for target in SEARCH_TARGETS:
            filltered_files.append(
                open(f'{LOG_DIR}/{target[1]}_fillterd_traffic.txt', 'w'))
            details_files.append(
                open(f'{LOG_DIR}/{target[1]}_attribute_details.txt', 'w'))
        with open(DATA_PATH, 'r') as input:
            for line in input:
                items = line.split('\t')
                # トラフィック全体のカウンタを更新
                total_counter['total_traffic'] += 1
                if items[TrafficAttributes.LABEL] != '1':
                    total_counter['total_attack'] += 1

                # 検索属性ごとの処理
                for i, target in enumerate(SEARCH_TARGETS):
                    if items[target.index] != '0':
                        filltered_files[i].write(line)
                        target_detail_counters[i][items[target.index]] += 1

                        # 検索属性ごとのカウンタを更新
                        target_counters[i]['target'] += 1
                        if items[TrafficAttributes.LABEL] != '1':
                            target_counters[i]['attack'] += 1

        # 詳細ログに書き込み
        for i, target in enumerate(SEARCH_TARGETS):
            details_files[i].write('detail\tcount\n')
            for target, count in target_detail_counters[i].items():
                details_files[i].write(f'{target}\t{count}\n')

        # 結果を出力
        lines = []
        for item, count in total_counter.items():
            lines.append(f'{item} : {count}\n')
        for i, target in enumerate(SEARCH_TARGETS):
            lines.append(f'{target.name}\n')
            lines.append(f'\ttarget : {target_counters[i]["target"]}\n')
            lines.append(f'\tattack : {target_counters[i]["attack"]}\n')
            lines.append(f'\tattack rate : {
                target_counters[i]["attack"] / target_counters[i]["target"]}\n')
        with open(f'{OUT_DIR}/result.txt', 'w') as output:
            output.writelines(lines)
        print(''.join(lines))

    finally:
        for input in filltered_files:
            input.close()
        for input in details_files:
            input.close()


if __name__ == '__main__':
    main()
