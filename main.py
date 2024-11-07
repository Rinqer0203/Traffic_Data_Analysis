from os import makedirs
from collections import Counter
from traffic_attributes import TrafficAttributes


DATA_PATH = r".\data\20150101.txt"
FILLTERD_TRAFFIC_LOG_PATH = r".\log\filtered_traffic.txt"  # 検索で絞り込まれたログを保存するファイル
ATTRIBUTE_DETAILS_LOG_PATH = r".\log\attribute_details.txt"  # 検索対象の詳細を保存するファイル
SEARCH_INDEX = TrafficAttributes.MALWARE_DETECTION


def process_file(input_path: str) -> Counter:
    makedirs("./log", exist_ok=True)
    counter = Counter()
    search_target_counter = Counter()

    with open(FILLTERD_TRAFFIC_LOG_PATH, 'w') as fillterd_traffic_log:
        with open(input_path, 'r') as f:
            for line in f:
                counter["traffic"] += 1
                items = line.split('\t')
                if items[TrafficAttributes.LABEL] != "1":
                    counter["total_attack"] += 1

                if items[SEARCH_INDEX] != "0":
                    fillterd_traffic_log.write(line)
                    search_target = items[SEARCH_INDEX]
                    search_target_counter[search_target] += 1
                    counter["target"] += 1

                    if items[TrafficAttributes.LABEL] != "1":
                        counter["attack"] += 1

    with open(ATTRIBUTE_DETAILS_LOG_PATH, 'w') as attribute_details_log:
        for target, count in search_target_counter.items():
            attribute_details_log.write(f"{target} : {count}\n")

    return counter


def main():
    counter = process_file(DATA_PATH)

    for item, count in counter.items():
        print(f"{item} : {count}")
    print(f"attack rate : {counter['attack'] / counter['target']}")


if __name__ == "__main__":
    main()
