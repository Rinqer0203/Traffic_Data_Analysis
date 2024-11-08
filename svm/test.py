import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report

PATH = './data/with_header/20150101.txt'

# データ読み込み
data = pd.read_csv(PATH, delimiter='\t')

# カテゴリカルデータの変換
categorical_cols = ['IDS_DETECTION', 'MALWARE_DETECTION', 'ASHULA_DETECTION', 'SERVICE', 'FLAG', 'PROTOCOL']
data = pd.get_dummies(data, columns=categorical_cols, drop_first=True)

# ターゲットと特徴量に分ける
X = data.drop(columns=['LABEL', 'SOURCE_IP_ADDRESS', 'DESTINATION_IP_ADDRESS', 'START_TIME'])
y = data['LABEL']

# ランダムサンプリングの実装（例: 10000サンプルをランダムに抽出）
sample_size = 10000  # サンプリングするデータの数
X_sampled = X.sample(n=sample_size, random_state=42)
y_sampled = y.loc[X_sampled.index]

# データ分割
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# スケーリング
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

print('学習')

# SVMモデルの定義と学習
model = SVC(kernel='rbf', C=1.0)
model.fit(X_train, y_train)

print('完了')

# 予測と評価
y_pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred))
