# 기준 날짜를 입력하면 오늘까지의 몇일이나 지났는지 출력하는 GUI 프로그램을 만들어줘. 

import tkinter as tk
from datetime import datetime

def calculate_days_since():
    try:
        # 입력된 날짜를 날짜 형식으로 변환
        input_date = entry.get()
        input_date = datetime.strptime(input_date, '%Y-%m-%d')

        # 현재 날짜를 얻음
        today = datetime.today()

        # 경과 일수 계산
        days_difference = (today - input_date).days

        # 결과 출력
        result_label.config(text=f"기준 날짜로부터 {days_difference}일이 경과했습니다.")

    except ValueError:
        result_label.config(text="올바른 날짜 형식이 아닙니다.")

# Tkinter 창 생성
root = tk.Tk()
root.title("날짜 경과 일수 계산기")

# 라벨 및 입력 상자 생성
label = tk.Label(root, text="기준 날짜를 입력하세요 (YYYY-MM-DD):")
label.pack(pady=10)

entry = tk.Entry(root)
entry.pack(pady=10)

# 버튼 생성
calculate_button = tk.Button(root, text="Calculate", command=calculate_days_since)
calculate_button.pack(pady=10)

# 결과 표시 라벨 생성
result_label = tk.Label(root, text="")
result_label.pack(pady=10)

# Tkinter 이벤트 루프 시작
root.mainloop()
