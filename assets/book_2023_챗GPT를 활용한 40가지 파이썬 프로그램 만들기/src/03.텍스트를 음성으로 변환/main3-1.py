import pyttsx3

# 한글 TTS 엔진을 설정합니다.
engine = pyttsx3.init()
engine.setProperty('rate', 150)  # 말하는 속도를 설정합니다.

# 텍스트를 읽어주는 함수를 정의합니다.
def speak(text):
    engine.say(text)
    engine.runAndWait()

# 텍스트를 입력받아 TTS로 변환합니다.
text = "안녕하세요 챗GPT로 만드는 파이썬 작품들 입니다."
speak(text)