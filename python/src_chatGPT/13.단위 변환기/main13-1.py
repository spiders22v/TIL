# 파이썬으로 온도와 미터 단위 변환 프로그램을 만들어줘.

def temperature_converter():
    print("1. 섭씨(Celsius)에서 화씨(Fahrenheit)로 변환")
    print("2. 화씨(Fahrenheit)에서 섭씨(Celsius)로 변환")

    choice = input("변환할 단위를 선택하세요 (1/2): ")

    if choice not in ['1', '2']:
        print("올바른 선택이 아닙니다.")
        return

    value = float(input("변환할 온도 값 입력: "))

    if choice == '1':
        result = (value * 9/5) + 32
        print(f"{value} 섭씨는 {result} 화씨입니다.")
    elif choice == '2':
        result = (value - 32) * 5/9
        print(f"{value} 화씨는 {result} 섭씨입니다.")

def length_converter():
    print("1. 미터(m)에서 킬로미터(km)로 변환")
    print("2. 킬로미터(km)에서 미터(m)로 변환")

    choice = input("변환할 단위를 선택하세요 (1/2): ")

    if choice not in ['1', '2']:
        print("올바른 선택이 아닙니다.")
        return

    value = float(input("변환할 길이 값 입력: "))

    if choice == '1':
        result = value / 1000
        print(f"{value} 미터는 {result} 킬로미터입니다.")
    elif choice == '2':
        result = value * 1000
        print(f"{value} 킬로미터는 {result} 미터입니다.")

if __name__ == "__main__":
    print("1. 온도 변환")
    print("2. 길이 변환")

    category_choice = input("변환할 카테고리를 선택하세요 (1/2): ")

    if category_choice == '1':
        temperature_converter()
    elif category_choice == '2':
        length_converter()
    else:
        print("올바른 선택이 아닙니다.")
