'''
パラメータ最適化のためのグリッドサーチを行う
'''
from sklearn.model_selection import GridSearchCV
from sklearn.svm import SVC
from utils import svm_utils


def main():
    # データの読み込みと前処理
    X, y = svm_utils.load_and_preprocess_data()
    X_train, X_test, y_train, y_test, _ = svm_utils.split_and_scale_data(X, y)

    param_grid = {
        'C': [0.1, 1, 10, 100],
        'gamma': [1, 0.1, 0.01, 0.001],
        'kernel': ['rbf']
    }
    grid = GridSearchCV(SVC(), param_grid, refit=True, verbose=2, cv=5, n_jobs=-1)
    grid.fit(X_train, y_train)

    # 最適なモデルの取得
    model = grid.best_estimator_

    # 最適なパラメータの表示
    print('Best parameters : ', grid.best_params_)
    print('Best score : ', grid.best_score_)

    # モデルの評価を出力
    svm_utils.evaluate_model(model, X_test, y_test)


if __name__ == '__main__':
    main()
