# 파이썬으로 숫자 맞추기 게임을 만들 거야. 1~100까지 무작위 숫자를 생성하고 내가 숫자를 입력하면 무작위 숫자랑 비교해서 숫자가 큰지 작은지 알려줘. 숫자를 맞추면 몇 회만에 맞췄는지 알려주고 게임을 종료해. 

import random

def guess_the_number():
    # 1에서 100까지의 무작위 숫자 생성
    secret_number = random.randint(1, 100)
    attempts = 0  # 시도 횟수를 저장하는 변수 초기화

    print("1에서 100까지의 숫자 중 하나를 생각했습니다. 맞춰보세요!")

    while True:
        user_guess = int(input("추측한 숫자를 입력하세요: "))
        attempts += 1  # 사용자의 각 시도마다 시도 횟수 증가

        if user_guess == secret_number:
            print(f"축하합니다! {attempts}회 만에 숫자를 맞추셨습니다.")
            break
        elif user_guess < secret_number:
            print("아쉽습니다. 더 큰 숫자를 입력하세요.")
        else:
            print("아쉽습니다. 더 작은 숫자를 입력하세요.")

if __name__ == "__main__":
    guess_the_number()