from collections import Counter

class AttributeIndex:
    DURATION = 0
    SERVICE = 1
    SOURCE_BYTES = 2
    DESTINATION_BYTES = 3
    COUNT = 4
    SAME_SRV_RATE = 5
    SERROR_RATE = 6
    SRV_SERROR_RATE = 7
    DST_HOST_COUNT = 8
    DST_HOST_SRV_COUNT = 9
    DST_HOST_SAME_SRC_PORT_RATE = 10
    DST_HOST_SERROR_RATE = 11
    DST_HOST_SRV_SERROR_RATE = 12
    FLAG = 13
    IDS_DETECTION = 14
    MALWARE_DETECTION = 15
    ASHULA_DETECTION = 16
    LABEL = 17
    SOURCE_IP_ADDRESS = 18
    SOURCE_PORT_NUMBER = 19
    DESTINATION_IP_ADDRESS = 20
    DESTINATION_PORT_NUMBER = 21
    START_TIME = 22
    DURATION_DUPLICATE = 23

PATH =  r"C:\Users\tomoki\Downloads\201501\Kyoto2016\2015\01\20150105.txt"
SEARCH_INDEX = AttributeIndex.IDS_DETECTION

counter = Counter()
target_values = set()

def print_line(items, search_index):
    print(items)
    print(f"index {search_index} : {items[search_index]}")

def wait_input():
    print("続行するには何かキーを押してください ...")
    input()

with open(PATH, 'r') as f:
    for line in f:    
        counter["line_cnt"] += 1
        items = line.split('\t')

        if items[SEARCH_INDEX] != "0":
            search_target = items[SEARCH_INDEX]
            target_values.add(search_target)
            counter["target_cnt"] += 1

            # Labelが正常ではない場合にlabel_cntをインクリメント
            if items[AttributeIndex.LABEL] != "1":
                counter["label_cnt"] += 1
        
        # print_line(items, search_index)
        # wait_input()

print("line count: ", counter["line_cnt"])
print("target count: ", counter["target_cnt"])
print("label count: ", counter["label_cnt"])
print("dictionary: ", target_values)