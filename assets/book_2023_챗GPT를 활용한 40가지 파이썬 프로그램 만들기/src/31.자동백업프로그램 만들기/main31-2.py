import os
from tkinter import *
from tkinter import filedialog
from distutils.dir_util import copy_tree

root = Tk()
root.geometry('300x200') # 프로그램의 크기를 설정합니다.
root.title('백업 프로그램')

source_dir = '' # 원본 폴더의 경로를 저장하는 변수입니다.
target_dir = '' # 백업 대상 폴더의 경로를 저장하는 변수입니다.

def choose_source_folder():
    global source_dir
    source_dir = filedialog.askdirectory() # 파일 대화상자를 통해 원본 폴더를 선택합니다.
    source_label.config(text=source_dir)

def choose_target_folder():
    global target_dir
    target_dir = filedialog.askdirectory() # 파일 대화상자를 통해 백업 대상 폴더를 선택합니다.
    target_label.config(text=target_dir)

def backup():
    if source_dir and target_dir:
        copy_tree(source_dir, target_dir) # distutils.dir_util의 copy_tree 함수를 사용하여 원본 폴더를 대상 폴더로 복사합니다.
        result_label.config(text="백업이 완료되었습니다!")
    else:
        result_label.config(text="원본 폴더와 대상 폴더를 선택해주세요.")

source_button = Button(root, text="원본 폴더 선택", command=choose_source_folder)
source_button.pack(pady=10)

source_label = Label(root, text="원본 폴더")
source_label.pack()

target_button = Button(root, text="대상 폴더 선택", command=choose_target_folder)
target_button.pack(pady=10)

target_label = Label(root, text="대상 폴더")
target_label.pack()

backup_button = Button(root, text="백업 시작", command=backup)
backup_button.pack(pady=10)

result_label = Label(root, text="")
result_label.pack()

root.mainloop()
