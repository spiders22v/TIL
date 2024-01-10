import requests
from bs4 import BeautifulSoup

code = input("종목 번호를 입력하세요: ")
url = f'https://finance.naver.com/item/main.nhn?code={code}'

res = requests.get(url)
soup = BeautifulSoup(res.content, 'html.parser')
price = soup.select_one('#content > div.section.trade_compare > table > tbody > tr:nth-child(1) > td:nth-child(2)')
print(f"현재 {code} 주가는 {price.text}입니다.")