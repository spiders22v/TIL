import requests
from bs4 import BeautifulSoup
import tkinter as tk

def get_stock_price():
    code = code_entry.get()
    url = f'https://finance.naver.com/item/main.nhn?code={code}'

    res = requests.get(url)
    soup = BeautifulSoup(res.content, 'html.parser')
    price = soup.select_one('#content > div.section.trade_compare > table > tbody > tr:nth-child(1) > td:nth-child(2)')
    result_label.config(text=f"현재 {code} 주가는 {price.text}입니다.")

root = tk.Tk()
root.title("주식 가격 조회 프로그램")

label = tk.Label(root, text="종목 번호를 입력하세요:")
label.pack()

code_entry = tk.Entry(root)
code_entry.pack()

button = tk.Button(root, text="조회", command=get_stock_price)
button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()
