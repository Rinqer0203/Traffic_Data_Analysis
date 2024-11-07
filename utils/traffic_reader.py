''' サンプルデータ
14.160069	other	2475	1468	2	1.00	1.00	0.38	0	0	0.00	0.00	0.00	SF	3-133-1(1),14782-1-17(1),7209-1-16(1)	0	349(1)	-1	fd95:ec1e:6a61:49ee:0191:4307:2301:036e	4567	fd95:ec1e:6a61:05d3:7dd2:270d:61ec:03f4	445	00:00:24	tcp
'''
from traffic_attributes import TrafficAttributes


def main():
    while True:
        print('読みたいトラフィックデータを入力してください...')
        data = input().split('\t')
        list = TrafficAttributes.get_attribute_list()
        for i, item in enumerate(data):
            # iからlistのattributeのindexが一致するものを取得
            # 念の為、item.indexとiが一致するか確認
            for item in list:
                if i == item.index:
                    print(f'[{i}] {item.name} : {data[i]}')
        print('\n')


if __name__ == '__main__':
    main()
