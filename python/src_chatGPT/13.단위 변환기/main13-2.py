# 파이썬으로 단위변환 프로그램을 GUI를 이용해서 만들어줘

import tkinter as tk
from tkinter import ttk

def temperature_converter():
    celsius_label.grid(row=3, column=0, sticky="E")
    fahrenheit_label.grid(row=3, column=2, sticky="E")
    celsius_entry.grid(row=3, column=1, padx=5, pady=5)
    fahrenheit_entry.grid(row=3, column=3, padx=5, pady=5)
    convert_button.grid(row=4, column=1, columnspan=3, pady=10)

    def convert_temperature():
        try:
            celsius_value = float(celsius_entry.get())
            fahrenheit_result.set((celsius_value * 9/5) + 32)
        except ValueError:
            fahrenheit_result.set("Invalid Input")

    convert_button.config(command=convert_temperature)

def length_converter():
    meter_label.grid(row=3, column=0, sticky="E")
    kilometer_label.grid(row=3, column=2, sticky="E")
    meter_entry.grid(row=3, column=1, padx=5, pady=5)
    kilometer_entry.grid(row=3, column=3, padx=5, pady=5)
    convert_button.grid(row=4, column=1, columnspan=3, pady=10)

    def convert_length():
        try:
            meter_value = float(meter_entry.get())
            kilometer_result.set(meter_value / 1000)
        except ValueError:
            kilometer_result.set("Invalid Input")

    convert_button.config(command=convert_length)

def show_converter():
    selected_category = category_combobox.get()
    
    if selected_category == "온도 변환":
        temperature_converter()
    elif selected_category == "길이 변환":
        length_converter()

# GUI 생성
root = tk.Tk()
root.title("단위 변환 프로그램")

# 카테고리 선택
category_label = tk.Label(root, text="카테고리 선택:")
category_label.grid(row=0, column=0, padx=5, pady=5, sticky="E")

categories = ["온도 변환", "길이 변환"]
category_combobox = ttk.Combobox(root, values=categories)
category_combobox.grid(row=0, column=1, padx=5, pady=5)
category_combobox.set("온도 변환")

# 결과 표시 레이블
celsius_label = tk.Label(root, text="섭씨(Celsius):")
fahrenheit_label = tk.Label(root, text="화씨(Fahrenheit):")
celsius_entry = tk.Entry(root)
fahrenheit_result = tk.StringVar()
fahrenheit_entry = tk.Entry(root, textvariable=fahrenheit_result, state="readonly")

meter_label = tk.Label(root, text="미터(m):")
kilometer_label = tk.Label(root, text="킬로미터(km):")
meter_entry = tk.Entry(root)
kilometer_result = tk.StringVar()
kilometer_entry = tk.Entry(root, textvariable=kilometer_result, state="readonly")

# 변환 버튼
convert_button = tk.Button(root, text="변환")

# 카테고리 선택 후 보여주기 버튼
show_converter_button = tk.Button(root, text="선택한 카테고리 보기", command=show_converter)
show_converter_button.grid(row=1, column=0, columnspan=2, pady=10)

root.mainloop()
