import pyupbit
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

# 1년 전의 시간을 구합니다.
to_date = datetime.now()
from_date = to_date - timedelta(days=365)

# 비트코인(BTC)의 일별 시세를 조회합니다.
df = pyupbit.get_ohlcv("KRW-BTC", interval="day", to=to_date, count=365)

# 그래프의 x축 값을 지정합니다.
x_values = pd.date_range(start=from_date, end=to_date - timedelta(days=1), freq='D')

# 그래프를 그립니다.
plt.plot(x_values, df['close'])

# 그래프 제목과 레이블을 추가합니다.
plt.title('Bitcoin Price in KRW (1 year)')
plt.xlabel('Date')
plt.ylabel('Price (KRW)')

# x축 레이블을 45도로 회전합니다.
plt.xticks(rotation=45)

# 그래프를 보여줍니다.
plt.show()
