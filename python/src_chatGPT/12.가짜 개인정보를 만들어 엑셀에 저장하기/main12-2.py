# 1000개의 가짜 이름, 성별, 이메일, 전화번호를 엑셀에 저장하는 프로그램을 만들어줘. 가짜개인정보.xlsx 이름으로 저장해줘.  

from faker import Faker
import pandas as pd

# 한국어로 가짜 개인정보 생성을 위한 Faker 객체 생성
fake = Faker('ko_KR')

# 1000개의 가짜 개인정보 생성
data = {'이름': [], '성별': [], '이메일': [], '전화번호': []}
for _ in range(1000):
    data['이름'].append(fake.name())
    data['성별'].append(fake.random_element(elements=('남성', '여성')))
    data['이메일'].append(fake.email())
    data['전화번호'].append(fake.phone_number())

# 데이터프레임 생성
df = pd.DataFrame(data)

# 엑셀 파일로 저장
df.to_excel('가짜개인정보.xlsx', index=False)
print('가짜개인정보.xlsx 파일이 생성되었습니다.')
