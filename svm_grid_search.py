from sklearn.model_selection import GridSearchCV
from sklearn.svm import SVC
from utils.svm_utils import load_and_preprocess_data, evaluate_model


def main():
    # データの読み込みと前処理
    X_train, X_test, y_train, y_test = load_and_preprocess_data()

    # グリッドサーチの実行
    print("Performing grid search...")
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
    print('Best parameters found: ', grid.best_params_)
    print('Best cross-validation score: ', grid.best_score_)

    # モデルの評価を出力
    evaluate_model(model, X_test, y_test)


if __name__ == '__main__':
    main()
