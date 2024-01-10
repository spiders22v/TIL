# 챗봇 응답 함수
def chatbot_response(user_input):
    if user_input == "안녕":
        return "안녕하세요!"
    else:
        return "무슨 말씀이신지 잘 모르겠어요."

# 메인 함수
def main():
    print("안녕하세요! 챗봇입니다.")
    while True:
        user_input = input("사용자: ")
        response = chatbot_response(user_input)
        print("챗봇: " + response)

# 프로그램 실행
if __name__ == "__main__":
    main()
