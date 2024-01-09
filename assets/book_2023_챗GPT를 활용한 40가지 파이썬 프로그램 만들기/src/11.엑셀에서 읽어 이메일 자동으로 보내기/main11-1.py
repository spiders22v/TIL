# 파이썬으로 이메일.xlsx 엑셀 파일의 A열에는 이메일이 저장되어 있고, B열에는 이름이 저장되어 있어. 이메일과 이름을 출력하는 코드를 작성해줘

import pandas as pd

# Excel 파일 읽기
df = pd.read_excel('이메일.xlsx')

# A열에 있는 이메일 주소와 B열에 있는 이름 출력
for index, row in df.iterrows():
    email = row['이메일']  # '이메일 주소'는 실제 엑셀 파일의 A열 제목입니다.
    name = row['이름']  # '이름'은 실제 엑셀 파일의 B열 제목입니다.
    print(f"이메일 주소: {email}, 이름: {name}")
