from collections import Counter
from traffic_attributes import TrafficAttributes


PATH = r"C:\Users\tomoki\Downloads\201501\Kyoto2016\2015\01\20150105.txt"
FILLTERD_TRAFFIC_LOG_NAME = r"log\filtered_traffic.txt"
ATTRIBUTE_DETAILS_LOG_NAME = r"log\attribute_details.txt"
SEARCH_INDEX = TrafficAttributes.MALWARE_DETECTION


def process_file(input_path, log_path=FILLTERD_TRAFFIC_LOG_NAME, count_path=ATTRIBUTE_DETAILS_LOG_NAME):
    counter = Counter()
    search_target_counter = Counter()

    with open(log_path, 'w') as log_file:
        with open(input_path, 'r') as f:
            for line in f:
                counter["traffic"] += 1
                items = line.split('\t')

                if items[SEARCH_INDEX] != "0":
                    search_target = items[SEARCH_INDEX]
                    log_file.write(line)
                    search_target_counter[search_target] += 1
                    counter["target"] += 1

                    if items[TrafficAttributes.LABEL] != "1":
                        counter["attack"] += 1

    with open(count_path, 'w') as count_file:
        for target, count in search_target_counter.items():
            count_file.write(f"{target} : {count}\n")

    return counter


def main():
    counter = process_file(PATH)

    for item, count in counter.items():
        print(f"{item} : {count}")
    print(f"attack rate : {counter['attack'] / counter['target']}")


if __name__ == "__main__":
    main()
