import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter.scrolledtext import ScrolledText
import os

class DockerfileGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Dockerfile Generator")
        self.create_widgets()

    def create_widgets(self):
        # 라벨, 콤보박스, 엔트리, 버튼, 스크롤 텍스트박스 생성
        self.label_base_image = ttk.Label(self.root, text="기본 이미지:")
        self.combobox_base_image = ttk.Combobox(self.root, values=["pytorch/pytorch", "tensorflow/tensorflow"], state="readonly")
        self.combobox_base_image.set("pytorch/pytorch")

        self.label_name = ttk.Label(self.root, text="이미지 이름:")
        self.entry_name = ttk.Entry(self.root, width=30)

        self.label_cmd = ttk.Label(self.root, text="실행 명령어:")
        self.entry_cmd = ttk.Entry(self.root, width=30)

        self.label_workdir = ttk.Label(self.root, text="작업 디렉토리:")
        self.entry_workdir = ttk.Entry(self.root, width=30)

        self.label_copy = ttk.Label(self.root, text="파일 복사:")
        self.entry_copy = ttk.Entry(self.root, width=30)

        self.button_generate = ttk.Button(self.root, text="도커파일 생성", command=self.generate_dockerfile)

        self.textbox_result = ScrolledText(self.root, wrap=tk.WORD, height=10, width=50)

        # 위젯 배치
        self.label_base_image.grid(row=0, column=0, pady=5, sticky="w")
        self.combobox_base_image.grid(row=0, column=1, pady=5, sticky="w")

        self.label_name.grid(row=1, column=0, pady=5, sticky="w")
        self.entry_name.grid(row=1, column=1, pady=5, sticky="w")

        self.label_cmd.grid(row=2, column=0, pady=5, sticky="w")
        self.entry_cmd.grid(row=2, column=1, pady=5, sticky="w")

        self.label_workdir.grid(row=3, column=0, pady=5, sticky="w")
        self.entry_workdir.grid(row=3, column=1, pady=5, sticky="w")

        self.label_copy.grid(row=4, column=0, pady=5, sticky="w")
        self.entry_copy.grid(row=4, column=1, pady=5, sticky="w")

        self.button_generate.grid(row=5, column=0, columnspan=2, pady=10)

        self.textbox_result.grid(row=6, column=0, columnspan=2, pady=5)

    def generate_dockerfile(self):
        # 사용자로부터 입력 받기
        base_image = self.combobox_base_image.get()
        image_name = self.entry_name.get()
        cmd = self.entry_cmd.get()
        workdir = self.entry_workdir.get()
        copy_files = self.entry_copy.get()

        # 입력이 비어있는지 확인
        if not image_name or not cmd:
            messagebox.showwarning("경고", "이미지 이름과 실행 명령어를 입력하세요.")
            return

        # 도커파일 생성
        dockerfile_content = f"FROM {base_image}\n"
        if workdir:
            dockerfile_content += f"WORKDIR {workdir}\n"
        if copy_files:
            copy_list = copy_files.split(",")
            for file in copy_list:
                dockerfile_content += f"COPY {file.strip()} .\n"
        dockerfile_content += f"CMD {cmd}"

        # 결과를 텍스트박스에 표시
        self.textbox_result.delete(1.0, tk.END)
        self.textbox_result.insert(tk.END, dockerfile_content)

        # 도커파일을 파일로 저장
        self.save_dockerfile(dockerfile_content)

    def save_dockerfile(self, content):
        try:
            with open("Dockerfile", "w", encoding="utf-8") as file:
                file.write(content)
            messagebox.showinfo("성공", "Dockerfile이 성공적으로 생성되었습니다.")
        except Exception as e:
            messagebox.showerror("오류", f"Dockerfile 생성 중 오류가 발생했습니다: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = DockerfileGeneratorApp(root)
    root.mainloop()
