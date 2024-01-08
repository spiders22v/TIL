# 파이썬 코드에서 실행에 필요한 라이브러리를 requirements.txt로 저장 

import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import messagebox
from pip._internal.operations.freeze import freeze

class RequirementsGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("Requirements.txt Generator")
        self.create_widgets()

    def create_widgets(self):
        # 라벨, 텍스트박스, 버튼 생성
        self.label_code = ttk.Label(self.root, text="파이썬 코드:")
        self.text_code = scrolledtext.ScrolledText(self.root, wrap=tk.WORD, height=10, width=50)
        self.button_generate = ttk.Button(self.root, text="Requirements.txt 생성", command=self.generate_requirements)

        # 위젯 배치
        self.label_code.grid(row=0, column=0, pady=5, sticky="w")
        self.text_code.grid(row=1, column=0, pady=5)
        self.button_generate.grid(row=2, column=0, pady=10)

    def generate_requirements(self):
        # 입력된 파이썬 코드 가져오기
        python_code = self.text_code.get("1.0", tk.END).strip()

        if not python_code:
            messagebox.showwarning("경고", "파이썬 코드를 입력하세요.")
            return

        try:
            # freeze를 사용하여 필요한 라이브러리 목록 추출
            requirements_list = freeze()
            
            # 필요한 라이브러리들을 requirements.txt 파일로 저장
            with open("requirements.txt", "w", encoding="utf-8") as file:
                file.write("\n".join(requirements_list))

            messagebox.showinfo("성공", "Requirements.txt 파일이 성공적으로 생성되었습니다.")
        except Exception as e:
            messagebox.showerror("오류", f"Requirements.txt 파일 생성 중 오류가 발생했습니다: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = RequirementsGenerator(root)
    root.mainloop()
