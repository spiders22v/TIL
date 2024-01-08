# 파이썬을 이용해서 한글 텍스트를 한글 음성으로 변환하는 코드를 작성해줘. 무료로 사용할 수 있는 pyttsx3 라이브러리를 사용해줘. 

import pyttsx3

def text_to_speech(text, lang='ko'):
    try:
        # pyttsx3 엔진 초기화
        engine = pyttsx3.init()

        # 한글 언어 설정
        engine.setProperty('rate', 150)  # 음성 속도 설정
        engine.setProperty('voice', 'ko')  # 한글 음성 선택

        # 텍스트를 음성으로 변환하여 재생
        engine.say(text)
        engine.runAndWait()
    except Exception as e:
        print(f"음성 변환 중 오류가 발생했습니다: {e}")

if __name__ == "__main__":
    input_text = input("음성으로 변환할 한글 텍스트를 입력하세요: ")
    text_to_speech(input_text)
