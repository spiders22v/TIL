from gtts import gTTS
from playsound import playsound

# 텍스트를 입력받습니다.
text = input('텍스트를 입력하세요: ')

# 한국어로 음성을 출력하도록 설정합니다.
tts = gTTS(text, lang='ko')

# 음성을 mp3 파일로 저장합니다.
tts.save('output.mp3')

# 저장한 mp3 파일을 재생합니다.ㅇ
playsound('output.mp3')