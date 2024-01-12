# 파이썬으로 비트코인 시세조회 프로그램을 만들어줘. pyupbit 라이브러리를 사용해줘.

import pyupbit

def get_bitcoin_price():
    try:
        # pyupbit을 사용하여 현재 비트코인 시세 조회
        price_data = pyupbit.get_current_price("KRW-BTC")
        return price_data

    except Exception as e:
        return f"비트코인 시세 조회 중 오류 발생: {e}"

if __name__ == "__main__":
    # 비트코인 시세 조회
    result = get_bitcoin_price()

    # 결과 출력
    if isinstance(result, float):
        print(f"비트코인의 현재 시세: {result} 원")
    else:
        print(result)
