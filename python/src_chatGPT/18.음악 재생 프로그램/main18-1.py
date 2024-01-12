# 파이썬으로 "안녕하세요", "반갑습니다", "오늘은 날씨가 좋네요"를 음성으로 출력하는 mp3 파일을 만들어줘. gtts를 이용해줘.

from gtts import gTTS

# 각 문장을 리스트에 저장
sentences = ["안녕하세요", "반갑습니다", "오늘은 날씨가 좋네요"]

# 문장별로 mp3 파일 생성
for i, sentence in enumerate(sentences):
    tts = gTTS(text=sentence, lang='ko')
    filename = str(i+1) + "번 " + sentence + ".mp3"
    tts.save('18.음악 재생 프로그램\\' + filename)