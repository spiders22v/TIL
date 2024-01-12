
# 파이썬으로 분류 머신러닝 프로그램을 만들어줘.

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
from sklearn.datasets import load_iris

# Iris 데이터셋 로드
iris = load_iris()
X = iris.data
y = iris.target

# 데이터셋을 훈련 세트와 테스트 세트로 분할
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 랜덤 포레스트 분류 모델 생성
model = RandomForestClassifier(n_estimators=100, random_state=42)

# 모델을 훈련 세트로 훈련
model.fit(X_train, y_train)

# 테스트 세트에 대한 예측
y_pred = model.predict(X_test)

# 정확도 및 분류 보고서 출력
accuracy = accuracy_score(y_test, y_pred)
print(f"정확도: {accuracy:.2f}")
print("\n분류 보고서:\n", classification_report(y_test, y_pred))


# 예제에서는 붓꽃(Iris) 데이터셋을 사용하여 붓꽃의 종류를 분류하는 모델을 만듦
# 이 코드는 RandomForestClassifier를 사용하여 Iris 데이터셋의 붓꽃을 분류하는 간단한 예제입니다. 
# 실제로 사용할 데이터에 맞게 데이터를 전처리하고 모델의 하이퍼파라미터를 조정해야 할 수 있습니다. 

# 실행 결과로는 정확도와 분류 보고서가 출력됩니다. 
# 정확도는 모델이 얼마나 정확하게 분류하는지를 나타내며, 
# 분류 보고서는 클래스별로 정밀도, 재현율, F1 점수 등을 보여줌