import psutil
import tkinter as tk

# 윈도우를 생성합니다.
window = tk.Tk()
window.title("시스템 모니터")

# CPU 사용량을 표시할 라벨을 생성합니다.
cpu_label = tk.Label(window, text="CPU 사용량: ")
cpu_label.pack()

# RAM 사용량을 표시할 라벨을 생성합니다.
ram_label = tk.Label(window, text="RAM 사용량: ")
ram_label.pack()

# 무한루프를 돌며 CPU, RAM 사용량을 업데이트합니다.
def update_usage():
    # CPU 사용량을 구하고 라벨에 업데이트합니다.
    cpu_percent = psutil.cpu_percent(interval=None)
    cpu_label.config(text=f"CPU 사용량: {cpu_percent}%")

    # RAM 사용량을 구하고 라벨에 업데이트합니다.
    mem = psutil.virtual_memory()
    mem_percent = mem.percent
    ram_label.config(text=f"RAM 사용량: {mem_percent}%")

    # 1초 대기합니다.
    window.after(1000, update_usage)

# 무한루프를 돌며 GUI를 업데이트합니다.
update_usage()

# 윈도우를 실행합니다.
window.mainloop()
