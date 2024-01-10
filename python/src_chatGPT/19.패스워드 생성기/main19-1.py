import random
import string

def generate_password():
    # 문자, 숫자, 특수문자를 모두 포함한 길이 12의 패스워드 생성
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(12))
    return password

# 패스워드 생성 함수 호출
password = generate_password()

print("생성된 패스워드: ", password)
