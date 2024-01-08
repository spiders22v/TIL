from sklearn.datasets import load_boston
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
import numpy as np

# 데이터 로드
boston = load_boston()
X = boston.data
y = boston.target

# 데이터 분리
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 모델 학습
reg = LinearRegression()
reg.fit(X_train, y_train)

# 모델 평가
y_pred = reg.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred)
print("실행결과")
print("="*80)
print(f"Mean squared error: {mse}")
print(f"Root mean squared error: {rmse}")
print(f"R^2 score: {r2}")
print("="*80)
from sklearn.model_selection import cross_val_score

# 교차 검증
scores = cross_val_score(reg, X, y, cv=5)
print("교차검증")
print("="*80)
print(f"Cross-validation scores: {scores}")
print(f"Average score: {scores.mean()}")
print("="*80)