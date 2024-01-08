import openpyxl
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# 이메일 설정
your_email_address = "your_email_address@example.com"  # 본인의 이메일 주소
your_email_password = "your_email_password"  # 본인의 이메일 비밀번호
smtp_server = "smtp.naver.com"  # SMTP 서버 주소
smtp_port = 587  # SMTP 서버 포트 번호

# 엑셀 파일 열기
wb = openpyxl.load_workbook('11.엑셀에서 읽어 이메일 자동으로 보내기\이메일.xlsx')
sheet = wb.active

# 각 행의 이메일과 이름에 대해 메일 보내기
for row in sheet.iter_rows(min_row=2, values_only=True):  # 첫 번째 행은 제외
    email, name = row

    # 이메일 내용 작성
    subject = f"{name}님 환영합니다."
    body = f"{name}님 늦지 않게 와주세요."
    message = MIMEMultipart()
    message['From'] = your_email_address
    message['To'] = email
    message['Subject'] = subject
    message.attach(MIMEText(body, 'plain'))

    # 이메일 보내기
    with smtplib.SMTP(smtp_server, smtp_port) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.login(your_email_address, your_email_password)
        smtp.sendmail(your_email_address, email, message.as_string())

# 엑셀 파일 닫기
wb.close()
