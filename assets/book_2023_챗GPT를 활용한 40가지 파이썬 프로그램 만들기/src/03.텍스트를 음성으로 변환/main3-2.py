# 파이썬으로 gtts과 playsound을 사용해서 한글 텍스트를 한글 음성으로 변환하고 재생하는 코드를 작성해줘.  

from gtts import gTTS
from playsound import playsound

def text_to_speech(text, lang='ko', file_name='output.mp3'):
    try:
        # 한글 텍스트를 한글 음성으로 변환
        tts = gTTS(text=text, lang=lang, slow=False)
        # 변환된 음성을 mp3 파일로 저장
        tts.save(file_name)

        # 생성된 mp3 파일을 재생
        playsound(file_name)
    except Exception as e:
        print(f"음성 변환 및 재생 중 오류가 발생했습니다: {e}")

if __name__ == "__main__":
    input_text = input("음성으로 변환할 한글 텍스트를 입력하세요: ")
    file_name = input("저장할 파일명을 입력하세요 (기본값: output.mp3): ") or 'output.mp3'
    text_to_speech(input_text, file_name=file_name)