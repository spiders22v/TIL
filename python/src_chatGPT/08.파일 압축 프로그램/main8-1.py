# 파이썬으로 파일을 압축하는 프로그램을 만들어줘

import zipfile
import os
from tkinter import Tk, filedialog

def zip_files(zip_filename, files_to_zip):
    with zipfile.ZipFile(zip_filename, 'w') as zipf:
        for file in files_to_zip:
            zipf.write(file, os.path.basename(file))

def main():
    # Tkinter를 사용하여 파일 선택 대화상자 열기
    root = Tk()
    root.withdraw()  # Tkinter 창 숨기기

    files_to_zip = filedialog.askopenfilenames(title='압축할 파일 선택', filetypes=[('All Files', '*.*')])

    if not files_to_zip:
        print('파일을 선택하지 않았습니다.')
        return

    # 압축 파일 이름 지정 및 경로 설정
    zip_filename = filedialog.asksaveasfilename(defaultextension=".zip", filetypes=[("Zip Files", "*.zip")], title='저장할 압축 파일 선택')

    if not zip_filename:
        print('저장할 압축 파일을 선택하지 않았습니다.')
        return

    # 파일 압축 실행
    zip_files(zip_filename, files_to_zip)
    print(f'압축이 완료되었습니다. 압축 파일: {zip_filename}')

if __name__ == '__main__':
    main()
