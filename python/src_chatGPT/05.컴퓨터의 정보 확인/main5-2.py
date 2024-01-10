# 파이썬으로 간단한 GUI를 이용해서 CPU, RAM, 네트워크의 사용량을 1초마다 출력하는 프로그램을 작성해줘. 

import psutil
import tkinter as tk
from tkinter import ttk

class SystemMonitorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("System Monitor")
        self.create_widgets()

    def create_widgets(self):
        # 라벨 및 프레임 생성
        self.label_cpu = ttk.Label(self.root, text="CPU 사용량:")
        self.label_ram = ttk.Label(self.root, text="RAM 사용량:")
        self.label_network = ttk.Label(self.root, text="네트워크 수신/전송:")
        
        self.frame = ttk.Frame(self.root, padding="10")

        # 라벨 및 프레임 배치
        self.label_cpu.grid(row=0, column=0, sticky="w")
        self.label_ram.grid(row=1, column=0, sticky="w")
        self.label_network.grid(row=2, column=0, sticky="w")
        self.frame.grid(row=3, column=0, columnspan=2)

        # 1초마다 시스템 정보 갱신
        self.update_system_stats()

    def update_system_stats(self):
        # CPU 사용량 및 코어 수 업데이트
        cpu_percent = psutil.cpu_percent()
        cpu_cores = psutil.cpu_count(logical=False)
        cpu_text = f"CPU 사용량: {cpu_percent}% (코어 수: {cpu_cores})"
        self.label_cpu.config(text=cpu_text)

        # RAM 사용량 업데이트
        ram_percent = psutil.virtual_memory().percent
        ram_text = f"RAM 사용량: {ram_percent}%"
        self.label_ram.config(text=ram_text)

        # 네트워크 사용량 업데이트
        network_stats = psutil.net_io_counters()
        network_text = f"네트워크 수신: {network_stats.bytes_recv} bytes, 전송: {network_stats.bytes_sent} bytes"
        self.label_network.config(text=network_text)

        # 1초 대기 후 재귀 호출
        self.root.after(1000, self.update_system_stats)

if __name__ == "__main__":
    root = tk.Tk()
    app = SystemMonitorApp(root)
    root.mainloop()
