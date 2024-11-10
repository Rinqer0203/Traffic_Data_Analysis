'''
SVMモデルを学習し、モデル, ダミー変数の列情報, スケーラーを保存する
'''
import joblib
import os
from sklearn.svm import SVC
from utils import svm_utils

# データのパス（フォルダでもファイルでも可）
LOAD_TSV_PATH = './data/Kyoto2016/2015/01'

# SVMモデルの保存先
MODEL_SAVE_PATH = './output/svm/svm_model.pkl'

# ダミー変数の列情報、スケーラーの保存先（評価時に必要になる）
DUMMY_COLUMNS_SAVE_PATH = './output/svm/dummy_columns.pkl'
SCALER_SAVE_PATH = './output/svm/scaler.pkl'


def main():
    X, y = svm_utils.load_and_preprocess_data(LOAD_TSV_PATH)
    X_train, X_test, y_train, y_test, scaler = svm_utils.split_and_scale_data(X, y)

    # SVMモデルの定義と学習
    model = SVC(kernel='rbf', C=100, gamma=0.1, random_state=42, verbose=True, max_iter=5000)
    model.fit(X_train, y_train)

    # モデル、ダミー変数の列情報、スケーラーの保存
    os.makedirs(os.path.dirname(MODEL_SAVE_PATH), exist_ok=True)
    joblib.dump(model, MODEL_SAVE_PATH)
    print(f'\nSaved {MODEL_SAVE_PATH}')
    joblib.dump(X.columns, DUMMY_COLUMNS_SAVE_PATH)
    print(f'Saved {DUMMY_COLUMNS_SAVE_PATH}')
    joblib.dump(scaler, SCALER_SAVE_PATH)
    print(f'Saved {SCALER_SAVE_PATH}')

    # モデルの評価を出力
    svm_utils.evaluate_model(model, X_test, y_test)


if __name__ == '__main__':
    main()
