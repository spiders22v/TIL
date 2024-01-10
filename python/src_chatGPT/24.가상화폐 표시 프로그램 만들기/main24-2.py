import pyupbit

# 모든 가상화폐의 티커(ticker) 리스트를 조회합니다.
tickers = pyupbit.get_tickers()

# 모든 가상화폐의 현재가를 조회하고 출력합니다.
for ticker in tickers:
    try:
        price = pyupbit.get_current_price(ticker)
        print(ticker, price)
    except:
        pass
