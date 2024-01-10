import random

# 사용자로부터 입력 받기
favorite_food = input("좋아하는 음식을 입력하세요: ")

# 추천할 음식 리스트 만들기
if favorite_food == "한식":
    food_list = ["비빔밥", "불고기", "갈비탕", "된장찌개", "김치찌개"]
elif favorite_food == "중식":
    food_list = ["짜장면", "짬뽕", "탕수육", "양장피", "마파두부"]
elif favorite_food == "일식":
    food_list = ["초밥", "라멘", "우동", "덮밥", "회"]
else:
    food_list = ["피자", "파스타", "햄버거", "치킨", "샐러드"]

# 추천할 음식 랜덤으로 선택하기
recommended_food = random.choice(food_list)

# 추천 결과 출력하기
print("추천하는 음식은", recommended_food, "입니다!")
