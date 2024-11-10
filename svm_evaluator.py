import joblib
import os
import pandas as pd
from utils import svm_utils

MODEL_SAVE_PATH = './output/svm/svm_model.pkl'
DUMMY_COLUMNS_SAVE_PATH = './output/svm/dummy_columns.pkl'
SCALER_SAVE_PATH = './output/svm/scaler.pkl'


def evaluate_saved_model(file_path: str):
    # モデル、ダミー変数の列情報、スケーラーの読み込み
    if not os.path.exists(MODEL_SAVE_PATH) or not os.path.exists(DUMMY_COLUMNS_SAVE_PATH) or not os.path.exists(SCALER_SAVE_PATH):
        print(f"Model, dummy columns, or scaler file not found at {
              MODEL_SAVE_PATH}, {DUMMY_COLUMNS_SAVE_PATH}, or {SCALER_SAVE_PATH}")
        return

    model = joblib.load(MODEL_SAVE_PATH)
    dummy_columns = joblib.load(DUMMY_COLUMNS_SAVE_PATH)
    scaler = joblib.load(SCALER_SAVE_PATH)
    print(f'Loaded model from {MODEL_SAVE_PATH}, dummy columns from {
          DUMMY_COLUMNS_SAVE_PATH}, and scaler from {SCALER_SAVE_PATH}')

    # データの読み込みと前処理
    X, y = svm_utils.load_and_preprocess_data(file_path)

    # ダミー変数の列をトレーニング時と一致させる
    X = X.reindex(columns=dummy_columns, fill_value=0)

    # データのスケーリング
    X = scaler.transform(X)

    # モデルの評価を出力
    svm_utils.evaluate_model(model, X, y)


if __name__ == '__main__':
    # 評価するファイルパスを指定
    file_path = './data/20150727.txt'
    evaluate_saved_model(file_path)
