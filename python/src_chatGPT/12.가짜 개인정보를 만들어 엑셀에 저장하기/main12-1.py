# 파이썬으로 가짜 한국어 개인정보를 만드는 코드 작성해줘

from faker import Faker

# 한국어로 가짜 개인정보 생성을 위한 Faker 객체 생성
fake = Faker('ko_KR')

# 가짜 이름, 주소, 전화번호, 이메일 등 생성
fake_name = fake.name()
fake_address = fake.address()
fake_phone_number = fake.phone_number()
fake_email = fake.email()

# 출력
print("가짜 이름:", fake_name)
print("가짜 주소:", fake_address)
print("가짜 전화번호:", fake_phone_number)
print("가짜 이메일:", fake_email)