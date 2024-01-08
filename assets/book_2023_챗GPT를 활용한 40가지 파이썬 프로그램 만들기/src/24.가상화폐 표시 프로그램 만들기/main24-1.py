import pyupbit

# 원화 시장에서 BTC/KRW의 현재가를 조회합니다.
price = pyupbit.get_current_price("KRW-BTC")

# 조회한 현재가를 출력합니다.
print("현재 BTC/KRW의 가격은", price, "원입니다.")
