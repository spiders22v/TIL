# 파이썬에서 웹페이지에서 이메일을 수집하는 코드를 만들어줘

import requests
from bs4 import BeautifulSoup
import re

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

# 수집된 이메일 출력
print("Extracted Emails:")
for email in extracted_emails:
    print(email)