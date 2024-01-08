from faker import Faker
from openpyxl import Workbook

fake = Faker('ko_KR')

# 엑셀 파일 생성
wb = Workbook()
ws = wb.active

# 헤더 추가
ws.append(['이름', '성별', '이메일', '전화번호'])

# 가짜 데이터 생성 및 저장
for i in range(1000):
    name = fake.name()
    gender = fake.random_element(elements=('남', '여'))
    email = fake.email()
    phone_number = fake.phone_number()
    ws.append([name, gender, email, phone_number])

# 엑셀 파일 저장
wb.save('12.가짜 개인정보를 만들어 엑셀에 저장하기/개인정보.xlsx')
