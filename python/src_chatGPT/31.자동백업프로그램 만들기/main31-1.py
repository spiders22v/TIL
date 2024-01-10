import os
from distutils.dir_util import copy_tree

source_dir = r'C:\0_project\173.챗GPT로 만드는 파이썬과 40개의 작품들\챗GPT로 만드는 파이썬 작품들\31.자동백업프로그램 만들기\원본폴더' # 복사할 폴더의 경로
target_dir = r'C:\0_project\173.챗GPT로 만드는 파이썬과 40개의 작품들\챗GPT로 만드는 파이썬 작품들\31.자동백업프로그램 만들기\백업폴더' # 복사될 대상 폴더의 경로

if not os.path.exists(target_dir):
    os.makedirs(target_dir) # 대상 폴더가 없을 경우 폴더를 생성합니다.

copy_tree(source_dir, target_dir) # source_dir의 모든 파일과 폴더를 target_dir로 복사합니다.

print("백업이 완료되었습니다!") # 백업이 완료되면 출력되는 메시지입니다.
