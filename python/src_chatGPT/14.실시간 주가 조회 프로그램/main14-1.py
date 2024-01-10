import requests
from bs4 import BeautifulSoup

code = '005930'
url = f'https://finance.naver.com/item/main.nhn?code={code}'

res = requests.get(url)
soup = BeautifulSoup(res.content, 'html.parser')
market_cap = soup.select_one('#content > div.section.trade_compare > table > tbody > tr:nth-child(1) > td:nth-child(2)')
print(market_cap.text)
