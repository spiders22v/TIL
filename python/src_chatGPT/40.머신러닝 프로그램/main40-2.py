# 파이썬 선형 회귀에 관한 머신러닝 프로그램을 만들어줘

import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt

plt.rcParams['font.family'] ='Malgun Gothic'
plt.rcParams['axes.unicode_minus'] =False

# 임의의 데이터 생성
np.random.seed(42)
X = 2 * np.random.rand(100, 1)
y = 4 + 3 * X + np.random.randn(100, 1)

# 데이터를 훈련 세트와 테스트 세트로 분할
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 선형 회귀 모델 생성 및 훈련
model = LinearRegression()
model.fit(X_train, y_train)

# 훈련된 모델을 사용하여 테스트 세트에 대한 예측
y_pred = model.predict(X_test)

# 성능 지표 출력
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print(f"평균 제곱 오차 (MSE): {mse:.2f}")
print(f"결정 계수 (R^2): {r2:.2f}")

# 테스트 세트와 예측 결과를 시각화
plt.scatter(X_test, y_test, color='black')
plt.plot(X_test, y_pred, color='blue', linewidth=3)
plt.xlabel('X')
plt.ylabel('y')
plt.title('선형 회귀 예측 결과')
plt.show()

# 이 코드는 1차원 입력 변수 X와 대응하는 출력 변수 y를 생성한 후, 선형 회귀 모델을 사용하여 학습하고 테스트 데이터에 대한 예측을 수행합니다. 모델의 성능 지표로 평균 제곱 오차(MSE)와 결정 계수(R^2)를 출력하며, 시각화를 통해 테스트 세트와 예측 결과를 비교합니다.