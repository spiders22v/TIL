while True:
    try:
        # 사용자로부터 변환하고자 하는 값과 단위를 입력받음
        value = float(input("변환하고자 하는 값을 입력하세요: "))
        unit = input("변환하고자 하는 단위를 입력하세요: ")
        
        # 입력받은 단위에 따라 변환 수행
        if unit == "C":
            fahrenheit = value * 9/5 + 32
            print("{0:.2f}℉".format(fahrenheit))
        elif unit == "F":
            celsius = (value - 32) * 5/9
            print("{0:.2f}℃".format(celsius))
        elif unit == "m":
            feet = value * 3.281
            print("{0:.2f}ft".format(feet))
        elif unit == "ft":
            meter = value / 3.281
            print("{0:.2f}m".format(meter))
        else:
            print("잘못된 입력입니다. 다시 시도해주세요.")
        
        # 다시 변환할 것인지 사용자에게 물어봄
        answer = input("다시 변환하시겠습니까? (Y/N)").upper()
        if answer == "N":
            break
    except ValueError:
        print("잘못된 입력입니다. 다시 시도해주세요.")
