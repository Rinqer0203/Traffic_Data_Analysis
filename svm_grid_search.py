from sklearn.model_selection import GridSearchCV
import pandas as pd
import joblib
import os
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report
from sampled_traffic_generator import get_sampled_data
from utils.tsv_header_adder import get_tsv_with_header
from utils.traffic_attributes import TrafficAttr

GRID_SEARCH_PATH = './output/svm/grid_search_results.pkl'


def main():
    # データ読み込み
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

    # グリッドサーチの実行または読み込み
    if os.path.exists(GRID_SEARCH_PATH):
        print("Loading grid search results from file...")
        grid = joblib.load(GRID_SEARCH_PATH)
    else:
        print("Performing grid search...")
        param_grid = {
            'C': [0.1, 1, 10, 100],
            'gamma': [1, 0.1, 0.01, 0.001],
            'kernel': ['rbf', 'linear']
        }
        grid = GridSearchCV(SVC(), param_grid, refit=True, verbose=2, cv=5, n_jobs=-1)
        grid.fit(X_train, y_train)
        joblib.dump(grid, GRID_SEARCH_PATH)

    # 最適なモデルの取得
    model = grid.best_estimator_

    # 最適なパラメータの表示
    print('Best parameters found: ', grid.best_params_)
    print('Best cross-validation score: ', grid.best_score_)

    # モデルの保存
    OUTPUT_PATH = './output/svm/svm_model.pkl'
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    joblib.dump(model, OUTPUT_PATH)
    print(f'Saved {OUTPUT_PATH}')

    # 予測と評価
    print('---評価---')
    y_pred = model.predict(X_test)
    print("Accuracy:", accuracy_score(y_test, y_pred))
    print(classification_report(y_test, y_pred))


if __name__ == '__main__':
    main()
