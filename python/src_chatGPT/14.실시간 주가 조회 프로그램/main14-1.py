# 파이썬으로 실시간 주식조회 프로그램을 만들어줘.

import requests
from bs4 import BeautifulSoup

code = '005930'  # 삼성전자
url = f'https://finance.naver.com/item/main.nhn?code={code}'

res = requests.get(url)
soup = BeautifulSoup(res.content, 'html.parser')
market_cap = soup.select_one('#content > div.section.trade_compare > table > tbody > tr:nth-child(1) > td:nth-child(2)')
print(market_cap.text)

