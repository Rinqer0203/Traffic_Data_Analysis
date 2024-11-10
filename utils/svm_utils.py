import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from utils.traffic_sampler import get_sampled_data
from utils.tsv_header_adder import get_tsv_with_header
from utils.traffic_attributes import TrafficAttr
from sklearn.metrics import accuracy_score, classification_report

# 使用する数値データの特徴量
NUMERIC_FEATURES = [
    TrafficAttr.DURATION.name,
    TrafficAttr.SOURCE_BYTES.name,
    TrafficAttr.DESTINATION_BYTES.name,
    TrafficAttr.COUNT.name,
    TrafficAttr.SAME_SRV_RATE.name,
    TrafficAttr.SERROR_RATE.name,
    TrafficAttr.SRV_SERROR_RATE.name,
    TrafficAttr.DST_HOST_COUNT.name,
    TrafficAttr.DST_HOST_SRV_COUNT.name,
    TrafficAttr.DST_HOST_SAME_SRC_PORT_RATE.name,
    TrafficAttr.DST_HOST_SERROR_RATE.name,
    TrafficAttr.DST_HOST_SRV_SERROR_RATE.name,
]

# 使用するカテゴリカルデータの特徴量（空リストでも可）
CATEGORICAL_FEATURES = [
    # TrafficAttr.IDS_DETECTION.name,
    # TrafficAttr.MALWARE_DETECTION.name,
    # TrafficAttr.ASHULA_DETECTION.name,
    # TrafficAttr.SERVICE.name,
    # TrafficAttr.FLAG.name,
    # TrafficAttr.PROTOCOL.name,
]


def load_and_preprocess_data(file_path: str | None = None):
    data = pd.read_csv(get_tsv_with_header(get_sampled_data(file_path)), delimiter='\t')

    # カテゴリカルデータをダミー変数に変換
    data = pd.get_dummies(data, columns=CATEGORICAL_FEATURES, drop_first=True)

    # 不要な特徴量を削除
    all_features = set(TrafficAttr.get_attribute_name_list())
    required_features = set(NUMERIC_FEATURES + CATEGORICAL_FEATURES + [TrafficAttr.LABEL.name])
    drop_features = list(all_features - required_features)
    data = data.drop(columns=drop_features)

    y = data[TrafficAttr.LABEL.name]
    X = data.drop(columns=[TrafficAttr.LABEL.name])
    return X, y


def split_and_scale_data(X, y):
    # データ分割
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # スケーリング
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    return X_train, X_test, y_train, y_test, scaler


def evaluate_model(model, X_test, y_test):
    y_pred = model.predict(X_test)
    print("Accuracy:", accuracy_score(y_test, y_pred))
    print(classification_report(y_test, y_pred))
