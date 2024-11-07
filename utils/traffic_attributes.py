from typing import NamedTuple


class Attribute(NamedTuple):
    index: int
    name: str


class TrafficAttributes:
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
    IDS_DETECTION = 14  # 0: Normal, 1: Alert
    MALWARE_DETECTION = 15  # 0: Normal, 1: Name
    ASHULA_DETECTION = 16  # 0: Normal, 1: Name
    LABEL = 17  # 1: Normal, -1: Known Attack, -2: Unknown Attack
    SOURCE_IP_ADDRESS = 18
    SOURCE_PORT_NUMBER = 19
    DESTINATION_IP_ADDRESS = 20
    DESTINATION_PORT_NUMBER = 21
    START_TIME = 22
    PROTOCOL = 23

    def get_attribute_list() -> list:
        return [
            Attribute(TrafficAttributes.DURATION, 'DURATION'),
            Attribute(TrafficAttributes.SERVICE, 'SERVICE'),
            Attribute(TrafficAttributes.SOURCE_BYTES, 'SOURCE_BYTES'),
            Attribute(TrafficAttributes.DESTINATION_BYTES, 'DESTINATION_BYTES'),
            Attribute(TrafficAttributes.COUNT, 'COUNT'),
            Attribute(TrafficAttributes.SAME_SRV_RATE, 'SAME_SRV_RATE'),
            Attribute(TrafficAttributes.SERROR_RATE, 'SERROR_RATE'),
            Attribute(TrafficAttributes.SRV_SERROR_RATE, 'SRV_SERROR_RATE'),
            Attribute(TrafficAttributes.DST_HOST_COUNT, 'DST_HOST_COUNT'),
            Attribute(TrafficAttributes.DST_HOST_SRV_COUNT, 'DST_HOST_SRV_COUNT'),
            Attribute(TrafficAttributes.DST_HOST_SAME_SRC_PORT_RATE, 'DST_HOST_SAME_SRC_PORT_RATE'),
            Attribute(TrafficAttributes.DST_HOST_SERROR_RATE, 'DST_HOST_SERROR_RATE'),
            Attribute(TrafficAttributes.DST_HOST_SRV_SERROR_RATE, 'DST_HOST_SRV_SERROR_RATE'),
            Attribute(TrafficAttributes.FLAG, 'FLAG'),
            Attribute(TrafficAttributes.IDS_DETECTION, 'IDS_DETECTION'),
            Attribute(TrafficAttributes.MALWARE_DETECTION, 'MALWARE_DETECTION'),
            Attribute(TrafficAttributes.ASHULA_DETECTION, 'ASHULA_DETECTION'),
            Attribute(TrafficAttributes.LABEL, 'LABEL'),
            Attribute(TrafficAttributes.SOURCE_IP_ADDRESS, 'SOURCE_IP_ADDRESS'),
            Attribute(TrafficAttributes.SOURCE_PORT_NUMBER, 'SOURCE_PORT_NUMBER'),
            Attribute(TrafficAttributes.DESTINATION_IP_ADDRESS, 'DESTINATION_IP_ADDRESS'),
            Attribute(TrafficAttributes.DESTINATION_PORT_NUMBER, 'DESTINATION_PORT_NUMBER'),
            Attribute(TrafficAttributes.START_TIME, 'START_TIME'),
            Attribute(TrafficAttributes.PROTOCOL, 'PROTOCOL')
        ]

    def get_attribute_name_list() -> list:
        return [item.name for item in TrafficAttributes.get_attribute_list()]


if __name__ == '__main__':
    # 簡易テスト
    list = TrafficAttributes.get_attribute_list()
    before_index = -1
    for item in list:
        print(f'{item.index}: {item.name}')
        # before_indexが昇順で連番になっていることを確認
        assert before_index == item.index - 1, 'Indexに不正があります'
        before_index = item.index
    print('テストOK')
