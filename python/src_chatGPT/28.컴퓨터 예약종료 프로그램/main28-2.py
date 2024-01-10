import os
import tkinter as tk
import tkinter.messagebox

class ShutdownApp:
    def __init__(self, master):
        self.master = master
        master.title("컴퓨터 예약종료")
        master.geometry("300x200")
        master.resizable(False, False)

        self.minutes_label = tk.Label(master, text="종료 예약할 시간(분):")
        self.minutes_label.pack(pady=10)

        self.minutes_entry = tk.Entry(master, width=10)
        self.minutes_entry.pack(pady=10)

        self.cancel_button = tk.Button(master, text="예약 취소", command=self.cancel_shutdown)
        self.cancel_button.pack(pady=10)

        self.shutdown_button = tk.Button(master, text="종료 예약", command=self.shutdown)
        self.shutdown_button.pack(pady=10)

    def shutdown(self):
        """컴퓨터를 종료하는 함수"""
        minutes = self.minutes_entry.get()
        if minutes.isdigit() and int(minutes) > 0:
            os.system(f"shutdown /s /t {int(minutes) * 60}")
            message = f"{minutes}분 후에 컴퓨터가 종료됩니다."
            self.show_message(message)
        else:
            message = "올바른 값을 입력하세요."
            self.show_message(message)

    def cancel_shutdown(self):
        """컴퓨터 종료 예약을 취소하는 함수"""
        os.system("shutdown /a")
        self.show_message("컴퓨터 종료 예약이 취소되었습니다.")

    def show_message(self, message):
        """메시지를 보여주는 함수"""
        tk.messagebox.showinfo("알림", message)

if __name__ == "__main__":
    root = tk.Tk()
    app = ShutdownApp(root)
    root.mainloop()
