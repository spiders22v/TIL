# pip install pyaudio

import speech_recognition as sr

# 마이크에서 음성을 받아들입니다.
r = sr.Recognizer()
with sr.Microphone() as source:
    print("말씀해주세요.")
    audio = r.listen(source)

# 인식된 음성에서 텍스트를 추출합니다.
text = r.recognize_google(audio, language='ko-KR')

print(text)
