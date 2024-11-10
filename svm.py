import joblib
import os
from sklearn.svm import SVC
from utils.svm_utils import load_and_preprocess_data, evaluate_model

OUTPUT_PATH = './output/svm/svm_model.pkl'


def main():
    # データの読み込みと前処理
    X_train, X_test, y_train, y_test = load_and_preprocess_data()

    # SVMモデルの定義と学習
    model = SVC(kernel='rbf', C=100, gamma=0.1, random_state=42, verbose=True, max_iter=5000)
    model.fit(X_train, y_train)

    # モデルの保存
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    joblib.dump(model, OUTPUT_PATH)
    print(f'\nSaved {OUTPUT_PATH}')

    # モデルの評価を出力
    evaluate_model(model, X_test, y_test)


if __name__ == '__main__':
    main()
