import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sampled_traffic_generator import get_sampled_data
from utils.tsv_header_adder import get_tsv_with_header
from utils.traffic_attributes import TrafficAttr
from sklearn.metrics import accuracy_score, classification_report


def load_and_preprocess_data():
    data = pd.read_csv(get_tsv_with_header(get_sampled_data()), delimiter='\t')

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

    # データ分割
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # スケーリング
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    return X_train, X_test, y_train, y_test


def evaluate_model(model, X_test, y_test):
    y_pred = model.predict(X_test)
    print("Accuracy:", accuracy_score(y_test, y_pred))
    print(classification_report(y_test, y_pred))
