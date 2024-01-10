# 엑셀 파일에서 읽은 이메일 주소로 메일을 보내는 프로그램을 작성해줘. 제목은 읽은 이름 + 님 환영합니다. 네용은 이름 + 님 늦지 않게 와 주세요. 로 작성해줘. 코드에서 이메일 주소와 비밀번호를 바로 입력할 수 있도록 작성해줘

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(receiver_email, name):
    # Gmail 계정 설정
    email_address = 'your_email@gmail.com'  # 본인의 Gmail 이메일 주소 입력
    email_password = 'your_password'  # 본인의 Gmail 비밀번호 입력

    # 이메일 내용 설정
    subject = f'{name} 님 환영합니다.'
    body = f'{name} 님, 늦지 않게 와 주세요.'
    
    # 이메일 구성
    message = MIMEMultipart()
    message['From'] = email_address
    message['To'] = receiver_email
    message['Subject'] = subject

    # 본문 추가
    message.attach(MIMEText(body, 'plain'))

    # SMTP 서버 연결 및 이메일 전송
    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(email_address, email_password)
        server.sendmail(email_address, receiver_email, message.as_string())

# 엑셀 파일에서 이메일 주소 읽기 (예시)
# 이 예제에서는 pandas 라이브러리를 사용합니다.
import pandas as pd

# 엑셀 파일 경로 지정
excel_path = '이메일주소.xlsx'  # 본인의 엑셀 파일 경로 입력

# 엑셀 파일 읽기
df = pd.read_excel(excel_path)

# 각 행에 대해 이메일 보내기
for index, row in df.iterrows():
    receiver_email = row['이메일 주소']  # '이메일 주소'는 실제 엑셀 파일의 열 제목입니다.
    name = row['이름']  # '이름'은 실제 엑셀 파일의 열 제목입니다.
    
    # 이메일 보내기
    send_email(receiver_email, name)

print("이메일이 전송되었습니다.")
