import random

# 1부터 100까지 무작위 숫자 생성
number = random.randint(1, 100)

# 몇 회 시도했는지를 저장하는 변수
num_of_guesses = 0

# 무한 반복문
while True:
    # 사용자로부터 숫자 입력 받기
    guess = int(input("1부터 100까지의 숫자를 입력하세요: "))
    
    # 시도 횟수 증가
    num_of_guesses += 1
    
    # 추측한 숫자가 정답보다 큰 경우
    if guess > number:
        print("입력한 숫자가 너무 큽니다.")
        
    # 추측한 숫자가 정답보다 작은 경우
    elif guess < number:
        print("입력한 숫자가 너무 작습니다.")
        
    # 추측한 숫자가 정답인 경우
    else:
        print(f"축하합니다! {num_of_guesses}회 만에 숫자를 맞췄습니다.")
        break