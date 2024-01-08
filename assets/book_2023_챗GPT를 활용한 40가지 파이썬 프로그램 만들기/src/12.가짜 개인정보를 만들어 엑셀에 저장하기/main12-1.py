from faker import Faker

fake = Faker('ko_KR')  # 한국어 가짜 데이터 생성

# 가짜 이름 생성
name = fake.name()

# 가짜 주소 생성
address = fake.address()

# 가짜 전화번호 생성
phone_number = fake.phone_number()

# 가짜 이메일 주소 생성
email = fake.email()

# 가짜 생년월일 생성
birthdate = fake.date_of_birth()

print(name, address, phone_number, email, birthdate)
