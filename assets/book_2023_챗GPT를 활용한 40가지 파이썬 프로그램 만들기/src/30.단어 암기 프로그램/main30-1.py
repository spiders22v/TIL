# random 모듈을 import합니다.
import random

# 영어 단어와 뜻이 들어있는 dictionary를 만듭니다.
dictionary = {
    "apple": "사과",
    "banana": "바나나",
    "carrot": "당근",
    "dog": "개",
    "elephant": "코끼리",
    "flower": "꽃",
    "guitar": "기타",
    "house": "집",
    "ice cream": "아이스크림",
    "jacket": "재킷"
}

# 퀴즈를 만드는 함수를 정의합니다.
def quiz():
    # dictionary에서 무작위로 단어와 뜻을 선택합니다.
    word, meaning = random.choice(list(dictionary.items()))
    
    # 사용자에게 단어의 뜻을 물어봅니다.
    answer = input(f"{word}의 뜻은 무엇일까요? ")
    
    # 사용자가 입력한 답과 정답을 비교하여 결과를 출력합니다.
    if answer == meaning:
        print("정답입니다!")
    else:
        print(f"틀렸습니다. 정답은 {meaning}입니다.")

# 메인 프로그램을 실행합니다.
if __name__ == "__main__":
    # 퀴즈를 5번 반복합니다.
    for i in range(5):
        quiz()
