from typing import NamedTuple
from enum import IntEnum


class Attr(NamedTuple):
    index: int
    name: str


class TrafficAttr(IntEnum):
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

    # def get_attribute_list() -> list:
    #     return [
    #         Attr(TrafficAttr.DURATION, 'DURATION'),
    #         Attr(TrafficAttr.SERVICE, 'SERVICE'),
    #         Attr(TrafficAttr.SOURCE_BYTES, 'SOURCE_BYTES'),
    #         Attr(TrafficAttr.DESTINATION_BYTES, 'DESTINATION_BYTES'),
    #         Attr(TrafficAttr.COUNT, 'COUNT'),
    #         Attr(TrafficAttr.SAME_SRV_RATE, 'SAME_SRV_RATE'),
    #         Attr(TrafficAttr.SERROR_RATE, 'SERROR_RATE'),
    #         Attr(TrafficAttr.SRV_SERROR_RATE, 'SRV_SERROR_RATE'),
    #         Attr(TrafficAttr.DST_HOST_COUNT, 'DST_HOST_COUNT'),
    #         Attr(TrafficAttr.DST_HOST_SRV_COUNT, 'DST_HOST_SRV_COUNT'),
    #         Attr(TrafficAttr.DST_HOST_SAME_SRC_PORT_RATE, 'DST_HOST_SAME_SRC_PORT_RATE'),
    #         Attr(TrafficAttr.DST_HOST_SERROR_RATE, 'DST_HOST_SERROR_RATE'),
    #         Attr(TrafficAttr.DST_HOST_SRV_SERROR_RATE, 'DST_HOST_SRV_SERROR_RATE'),
    #         Attr(TrafficAttr.FLAG, 'FLAG'),
    #         Attr(TrafficAttr.IDS_DETECTION, 'IDS_DETECTION'),
    #         Attr(TrafficAttr.MALWARE_DETECTION, 'MALWARE_DETECTION'),
    #         Attr(TrafficAttr.ASHULA_DETECTION, 'ASHULA_DETECTION'),
    #         Attr(TrafficAttr.LABEL, 'LABEL'),
    #         Attr(TrafficAttr.SOURCE_IP_ADDRESS, 'SOURCE_IP_ADDRESS'),
    #         Attr(TrafficAttr.SOURCE_PORT_NUMBER, 'SOURCE_PORT_NUMBER'),
    #         Attr(TrafficAttr.DESTINATION_IP_ADDRESS, 'DESTINATION_IP_ADDRESS'),
    #         Attr(TrafficAttr.DESTINATION_PORT_NUMBER, 'DESTINATION_PORT_NUMBER'),
    #         Attr(TrafficAttr.START_TIME, 'START_TIME'),
    #         Attr(TrafficAttr.PROTOCOL, 'PROTOCOL')
    #     ]

    def get_attribute_name_list() -> list:
        return list(TrafficAttr.__members__.keys())


if __name__ == '__main__':
    # 簡易テスト
    list = TrafficAttr.get_attribute_list()
    before_index = -1
    for item in list:
        print(f'{item.index}: {item.name}')
        # before_indexが昇順で連番になっていることを確認
        assert before_index == item.index - 1, 'Indexに不正があります'
        before_index = item.index
    print('テストOK')
