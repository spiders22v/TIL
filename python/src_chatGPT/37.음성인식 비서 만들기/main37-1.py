
# 파이썬으로 음성을 인식하여 텍스트로 변환하는 프로그램을 만들어줘. 한국어 음성이야. SpeechRecognition을 사용해서 작성해줘.

import speech_recognition as sr

def recognize_speech():
    recognizer = sr.Recognizer()

    # 마이크에서 음성을 듣기
    with sr.Microphone() as source:
        print("말해주세요...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source, timeout=5)

    try:
        print("음성을 텍스트로 변환 중...")
        text = recognizer.recognize_google(audio, language="ko-KR")
        print("인식된 텍스트:", text)
    except sr.UnknownValueError:
        print("음성을 인식할 수 없습니다.")
        text = ""
    except sr.RequestError as e:
        print(f"음성 인식에 오류가 발생했습니다. {e}")
        text = ""

    return text

if __name__ == "__main__":
    recognized_text = recognize_speech()
    if recognized_text:
        # 여기에서 recognized_text를 활용하여 원하는 동작을 수행할 수 있습니다.
        print("텍스트로 변환된 결과:", recognized_text)
    else:
        print("음성을 인식할 수 없습니다.")
