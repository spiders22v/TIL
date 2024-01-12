# 파이썬으로 로또번호 생성기 GUI 프로그램을 만들어줘.

import tkinter as tk
import random

def generate_lotto_numbers():
    # 1부터 45까지의 숫자 중에서 6개를 선택하여 반환
    lotto_numbers = random.sample(range(1, 46), 6)
    lotto_numbers.sort()
    result_label.config(text=f"로또 번호: {lotto_numbers}")

# Tkinter 창 생성
root = tk.Tk()
root.title("로또 번호 생성기")

# 버튼 생성
generate_button = tk.Button(root, text="로또 번호 생성", command=generate_lotto_numbers)
generate_button.pack(pady=10)

# 결과 표시 라벨 생성
result_label = tk.Label(root, text="")
result_label.pack(pady=10)

# Tkinter 이벤트 루프 시작
root.mainloop()
