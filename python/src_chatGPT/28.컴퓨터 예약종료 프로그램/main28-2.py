# 파이썬으로 컴퓨터 예약종료 GUI 프로그램을 만들어줘. GUI 크기는 300x200이야.

# import os
# import tkinter as tk
# import tkinter.messagebox

# class ShutdownApp:
#     def __init__(self, master):
#         self.master = master
#         master.title("컴퓨터 예약종료")
#         master.geometry("300x200")
#         master.resizable(False, False)

#         self.minutes_label = tk.Label(master, text="종료 예약할 시간(분):")
#         self.minutes_label.pack(pady=10)

#         self.minutes_entry = tk.Entry(master, width=10)
#         self.minutes_entry.pack(pady=10)

#         self.cancel_button = tk.Button(master, text="예약 취소", command=self.cancel_shutdown)
#         self.cancel_button.pack(pady=10)

#         self.shutdown_button = tk.Button(master, text="종료 예약", command=self.shutdown)
#         self.shutdown_button.pack(pady=10)

#     def shutdown(self):
#         """컴퓨터를 종료하는 함수"""
#         minutes = self.minutes_entry.get()
#         if minutes.isdigit() and int(minutes) > 0:
#             os.system(f"shutdown /s /t {int(minutes) * 60}")
#             message = f"{minutes}분 후에 컴퓨터가 종료됩니다."
#             self.show_message(message)
#         else:
#             message = "올바른 값을 입력하세요."
#             self.show_message(message)

#     def cancel_shutdown(self):
#         """컴퓨터 종료 예약을 취소하는 함수"""
#         os.system("shutdown /a")
#         self.show_message("컴퓨터 종료 예약이 취소되었습니다.")

#     def show_message(self, message):
#         """메시지를 보여주는 함수"""
#         tk.messagebox.showinfo("알림", message)

# if __name__ == "__main__":
#     root = tk.Tk()
#     app = ShutdownApp(root)
#     root.mainloop()

import tkinter as tk
import os
from datetime import datetime, timedelta

def schedule_shutdown():
    try:
        # 사용자가 입력한 시간을 분 단위로 변환
        minutes = int(entry.get())

        # 현재 시각에 사용자가 입력한 시간을 더한 시간을 구함
        shutdown_time = datetime.now() + timedelta(minutes=minutes)

        # 예약 종료 명령 실행
        command = f"shutdown -s -t {minutes * 60}"
        os.system(command)

        # 예약 종료 시간을 라벨에 표시
        result_label.config(text=f"컴퓨터 예약 종료 시간: {shutdown_time.strftime('%Y-%m-%d %H:%M:%S')}")

    except ValueError:
        result_label.config(text="올바른 시간을 입력하세요.")

# Tkinter 창 생성
root = tk.Tk()
root.title("컴퓨터 예약 종료 프로그램")
root.geometry("300x200")

# 라벨 및 입력 상자 생성
label = tk.Label(root, text="종료 예약 시간(분):")
label.pack(pady=10)

entry = tk.Entry(root)
entry.pack(pady=10)

# 버튼 생성
shutdown_button = tk.Button(root, text="종료 예약", command=schedule_shutdown)
shutdown_button.pack(pady=10)

# 결과 표시 라벨 생성
result_label = tk.Label(root, text="")
result_label.pack(pady=10)

# Tkinter 이벤트 루프 시작
root.mainloop()
