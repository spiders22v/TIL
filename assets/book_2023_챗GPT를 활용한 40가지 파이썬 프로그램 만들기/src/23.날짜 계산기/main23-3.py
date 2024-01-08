import tkinter as tk
import datetime

def calculate_days():
    start_date = datetime.date(int(year_entry.get()), int(month_entry.get()), int(day_entry.get()))
    end_date = datetime.date.today()
    days_diff = (end_date - start_date).days
    result_label.config(text=f"{start_date.strftime('%Y년 %m월 %d일')}부터 오늘까지 {days_diff}일이 지났습니다.")

root = tk.Tk()
root.title("날짜 계산기")

# 라벨 및 엔트리 위젯 생성
year_label = tk.Label(root, text="연도")
year_label.grid(row=0, column=0)
year_entry = tk.Entry(root)
year_entry.grid(row=0, column=1)

month_label = tk.Label(root, text="월")
month_label.grid(row=1, column=0)
month_entry = tk.Entry(root)
month_entry.grid(row=1, column=1)

day_label = tk.Label(root, text="일")
day_label.grid(row=2, column=0)
day_entry = tk.Entry(root)
day_entry.grid(row=2, column=1)

# 계산 버튼 생성
calculate_button = tk.Button(root, text="계산", command=calculate_days)
calculate_button.grid(row=3, column=0, columnspan=2)

# 결과 출력 라벨 생성
result_label = tk.Label(root, text="")
result_label.grid(row=4, column=0, columnspan=2)

root.mainloop()
