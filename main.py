from collections import Counter
from AttributeIndex import AttributeIndex


PATH = r"C:\Users\tomoki\Downloads\201501\Kyoto2016\2015\01\20150105.txt"
FILLTERD_TRAFFIC_LOG_NAME = r"log\filtered_traffic.txt"
ATTRIBUTE_DETAILS_LOG_NAME = r"log\attribute_details.txt"
SEARCH_INDEX = AttributeIndex.IDS_DETECTION


def process_file(input_path, log_path, count_path):
    counter = Counter()
    search_target_counter = Counter()

    with open(log_path, 'w') as log_file:
        with open(input_path, 'r') as f:
            for line in f:
                counter["traffic_cnt"] += 1
                items = line.split('\t')

                if items[SEARCH_INDEX] != "0":
                    search_target = items[SEARCH_INDEX]
                    log_file.write(line)
                    search_target_counter[search_target] += 1
                    counter["target_cnt"] += 1

                    if items[AttributeIndex.LABEL] != "1":
                        counter["attack_cnt"] += 1

    with open(count_path, 'w') as count_file:
        for target, count in search_target_counter.items():
            count_file.write(f"{target} : {count}\n")

    return counter


def main():
    counter = process_file(PATH, FILLTERD_TRAFFIC_LOG_NAME, ATTRIBUTE_DETAILS_LOG_NAME)

    for item, count in counter.items():
        print(f"{item} : {count}")


if __name__ == "__main__":
    main()
