''' 
---サンプルデータ---
14.160069	other	2475	1468	2	1.00	1.00	0.38	0	0	0.00	0.00	0.00	SF	3-133-1(1),14782-1-17(1),7209-1-16(1)	0	349(1)	-1	fd95:ec1e:6a61:49ee:0191:4307:2301:036e	4567	fd95:ec1e:6a61:05d3:7dd2:270d:61ec:03f4	445	00:00:24	tcp

---出力---
[0] DURATION : 14.160069
[1] SERVICE : other
[2] SOURCE_BYTES : 2475
[3] DESTINATION_BYTES : 1468
[4] COUNT : 2
[5] SAME_SRV_RATE : 1.00
[6] SERROR_RATE : 1.00
[7] SRV_SERROR_RATE : 0.38
[8] DST_HOST_COUNT : 0
[9] DST_HOST_SRV_COUNT : 0
[10] DST_HOST_SAME_SRC_PORT_RATE : 0.00
[11] DST_HOST_SERROR_RATE : 0.00
[12] DST_HOST_SRV_SERROR_RATE : 0.00
[13] FLAG : SF
[14] IDS_DETECTION : 3-133-1(1),14782-1-17(1),7209-1-16(1)
[15] MALWARE_DETECTION : 0
[16] ASHULA_DETECTION : 349(1)
[17] LABEL : -1
[18] SOURCE_IP_ADDRESS : fd95:ec1e:6a61:49ee:0191:4307:2301:036e
[19] SOURCE_PORT_NUMBER : 4567
[20] DESTINATION_IP_ADDRESS : fd95:ec1e:6a61:05d3:7dd2:270d:61ec:03f4
[21] DESTINATION_PORT_NUMBER : 445
[22] START_TIME : 00:00:24
[23] PROTOCOL : tcp
'''
from utils.traffic_attributes import TrafficAttr


def main():
    while True:
        print('読みたいトラフィックデータを入力してください...')
        data = input().split('\t')
        for i, item in enumerate(data):
            print(f'[{i}] {TrafficAttr(i).name} : {item}')
        print('\n')


if __name__ == '__main__':
    main()
