import tkinter as tk
import random

def generate_lotto_numbers():
    numbers = random.sample(range(1, 46), 6)
    numbers.sort()
    return numbers

def generate_and_display_numbers():
    numbers = generate_lotto_numbers()
    number_label.config(text=" ".join(str(num) for num in numbers))

# tkinter 윈도우 생성
window = tk.Tk()
window.title("로또 번호 생성기")
window.geometry("300x100")

# 버튼과 번호 출력 레이블 생성
button = tk.Button(text="번호 생성", command=generate_and_display_numbers)
number_label = tk.Label(text="")
number_label.pack()

# 버튼과 번호 출력 레이블 배치
button.pack(pady=10)
number_label.pack()

window.mainloop()
