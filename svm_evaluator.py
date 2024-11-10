'''
モデルの評価を行うスクリプト
'''
import joblib
import os
from utils import svm_utils

# 評価するデータのパス (フォルダでもファイルでも可)
EVALUATE_TSV_PATH = './data/201502/Kyoto2016/2015/02'

# モデル、ダミー変数の列情報、スケーラーのロード先
MODEL_LOAD_PATH = './output/svm/svm_model.pkl'
DUMMY_COLUMNS_LOAD_PATH = './output/svm/dummy_columns.pkl'
SCALER_LOAD_PATH = './output/svm/scaler.pkl'


def evaluate_saved_model(file_path: str):
    # モデル、ダミー変数の列情報、スケーラーの読み込み
    if not os.path.exists(MODEL_LOAD_PATH) or not os.path.exists(DUMMY_COLUMNS_LOAD_PATH) or not os.path.exists(SCALER_LOAD_PATH):
        print(f"Model, dummy columns, or scaler file not found at {
              MODEL_LOAD_PATH}, {DUMMY_COLUMNS_LOAD_PATH}, or {SCALER_LOAD_PATH}")
        return
    model = joblib.load(MODEL_LOAD_PATH)
    dummy_columns = joblib.load(DUMMY_COLUMNS_LOAD_PATH)
    scaler = joblib.load(SCALER_LOAD_PATH)

    # データの読み込みと前処理
    X, y = svm_utils.load_and_preprocess_data(file_path)

    # ダミー変数の列をトレーニング時と一致させる
    X = X.reindex(columns=dummy_columns, fill_value=0)

    # データのスケーリング
    X = scaler.transform(X)

    # モデルの評価を出力
    svm_utils.evaluate_model(model, X, y)


if __name__ == '__main__':
    evaluate_saved_model(EVALUATE_TSV_PATH)
