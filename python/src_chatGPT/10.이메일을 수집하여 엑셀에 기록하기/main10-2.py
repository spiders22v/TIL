# (main10-1 프롬프트에 이어서) 찾은 이메일 주소를 "이메일.xlsx"로 저장하는 코드를 작성해줘.

import requests
from bs4 import BeautifulSoup
import re
import pandas as pd

def extract_emails(url):
    # 웹페이지에서 HTML 내용을 가져옴
    response = requests.get(url)
    html_content = response.text

    # 이메일 주소를 정규식을 사용하여 추출
    emails = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', html_content)

    # 중복 이메일을 제거하기 위해 set으로 변환 후 다시 리스트로 변환
    unique_emails = list(set(emails))

    return unique_emails

# 이메일을 수집하고 싶은 웹페이지의 URL을 지정
webpage_url = 'https://v.daum.net/v/20230303140011566'
extracted_emails = extract_emails(webpage_url)

# 데이터프레임 생성
df = pd.DataFrame({'Emails': extracted_emails})

# Excel 파일로 저장
df.to_excel('이메일.xlsx', index=False)

print("이메일이 '이메일.xlsx' 파일로 저장되었습니다.")
