import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report
import tsv_header_adder
from utils.traffic_attributes import TrafficAttr

PATH = './output/sampled_traffic/sampled.txt'


def main():
    # データ読み込み
    data = pd.read_csv(tsv_header_adder.get_tsv_with_header(PATH), delimiter='\t')

    # カテゴリカルデータの変換
    categorical_cols = [
        TrafficAttr.IDS_DETECTION.name, TrafficAttr.MALWARE_DETECTION.name, TrafficAttr.ASHULA_DETECTION.name,
        TrafficAttr.SERVICE.name, TrafficAttr.FLAG.name, TrafficAttr.PROTOCOL.name
    ]
    data = pd.get_dummies(data, columns=categorical_cols, drop_first=True)

    # ターゲットと特徴量に分ける
    X = data.drop(columns=[
        TrafficAttr.LABEL.name, TrafficAttr.SOURCE_IP_ADDRESS.name, TrafficAttr.DESTINATION_IP_ADDRESS.name, TrafficAttr.START_TIME.name
    ])
    y = data[TrafficAttr.LABEL.name]

    # データ分割（ランダムサンプリングをなくし、全データを使用）
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # スケーリング
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    print('学習開始')

    # SVMモデルの定義と学習
    model = SVC(kernel='rbf', C=1.0, random_state=42, verbose=True, max_iter=5000)
    model.fit(X_train, y_train)

    print('完了')

    # 予測と評価
    y_pred = model.predict(X_test)
    print("Accuracy:", accuracy_score(y_test, y_pred))
    print(classification_report(y_test, y_pred))


if __name__ == '__main__':
    main()
