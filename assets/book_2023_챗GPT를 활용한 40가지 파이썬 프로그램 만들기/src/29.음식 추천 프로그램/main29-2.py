import random

# 사용자로부터 입력 받기
mood = input("오늘 기분은 어떠세요? (기쁨, 슬픔, 화남, 지침, 무기력): ")

# 추천할 음식 리스트 만들기
if mood == "기쁨":
    food_list = ["아이스크림", "케이크", "파이", "초콜릿", "딸기"]
elif mood == "슬픔":
    food_list = ["치즈케이크", "초콜릿케이크", "아이스크림", "초콜릿", "커피"]
elif mood == "화남":
    food_list = ["매운 음식", "떡볶이", "김치찌개", "된장찌개", "라면"]
elif mood == "지침":
    food_list = ["보양식", "감자탕", "삼계탕", "영양밥", "비빔밥"]
else:
    food_list = ["샐러드", "스무디", "과일", "토스트", "샌드위치"]

# 추천할 음식 랜덤으로 선택하기
recommended_food = random.choice(food_list)

# 추천 결과 출력하기
print("오늘 기분에 따라 추천하는 음식은", recommended_food, "입니다!")
