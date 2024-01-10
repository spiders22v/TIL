import os

def shutdown():
    """컴퓨터를 종료하는 함수"""
    os.system("shutdown /s /t 1")

def cancel_shutdown():
    """컴퓨터 종료 예약을 취소하는 함수"""
    os.system("shutdown /a")

def main():
    """프로그램의 메인 함수"""
    print("컴퓨터를 몇 분 후에 종료하시겠습니까?")
    print("(종료 예약을 취소하려면 '취소'라고 입력하세요.)")
    while True:
        user_input = input("분: ")
        if user_input.isdigit():
            minutes = int(user_input)
            if minutes > 0:
                os.system(f"shutdown /s /t {minutes * 60}")
                print(f"{minutes}분 후에 컴퓨터가 종료됩니다.")
                break
            else:
                print("0 이상의 숫자를 입력하세요.")
        elif user_input == "취소":
            cancel_shutdown()
            print("컴퓨터 종료 예약이 취소되었습니다.")
            break
        else:
            print("유효한 입력이 아닙니다. 다시 입력해주세요.")

if __name__ == "__main__":
    main()
