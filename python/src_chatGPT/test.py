print("Hello, World!")

import numpy as np

import matplotlib.pyplot as plt



# 0부터 2파이까지의 값을 0.1 간격으로 생성
x = np.arange(0, 2 * np.pi, 0.1)

# 사인과 코사인 값을 계산
y_sin = np.sin(x)
y_cos = np.cos(x)

# 그래프 생성 및 데이터 플로팅
plt.plot(x, y_sin, label='sin(x)')
plt.plot(x, y_cos, label='cos(x)')

# 그래프에 제목과 레이블 추가
plt.title('Sine and Cosine Functions')
plt.xlabel('x')
plt.ylabel('y')

# 범례 표시
plt.legend()

# 그래프 표시
plt.show()
