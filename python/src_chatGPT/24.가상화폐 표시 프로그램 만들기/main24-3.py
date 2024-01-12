# 파이썬으로 비트코인의 1년 금액 그래프를 그려줘. 1일 단위로 그려줘.

import pyupbit
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

plt.rcParams['font.family'] ='Malgun Gothic'
plt.rcParams['axes.unicode_minus'] =False

def get_bitcoin_prices(start_date, end_date):
    try:
        # pyupbit을 사용하여 비트코인 가격 일별 조회
        prices = pyupbit.get_ohlcv("KRW-BTC", interval="day", to=end_date, count=365)

        # 필요한 기간만 선택
        prices = prices.loc[start_date:end_date]

        return prices

    except Exception as e:
        return f"비트코인 가격 조회 중 오류 발생: {e}"

def plot_bitcoin_prices(prices):
    # 그래프 그리기
    plt.figure(figsize=(12, 6))
    plt.plot(prices.index, prices['close'], label='비트코인 가격', color='blue')
    plt.title('비트코인 가격 그래프 (1년)')
    plt.xlabel('날짜')
    plt.ylabel('가격 (원)')
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    # 1년 전부터 오늘까지의 날짜 계산
    end_date = datetime.now()
    start_date = end_date - timedelta(days=365)

    # 비트코인 가격 조회
    bitcoin_prices = get_bitcoin_prices(start_date, end_date)

    # 그래프 그리기
    plot_bitcoin_prices(bitcoin_prices)