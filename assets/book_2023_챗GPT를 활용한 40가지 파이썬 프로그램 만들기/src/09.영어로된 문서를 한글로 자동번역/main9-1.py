# 파이썬으로 "영어문서.txt"파일에서 영어를 한국어로 번역해서 "한글번역.txt" 파일에 저장하는 코드를 작성해줘.

from googletrans import Translator

def translate_file(input_file, output_file):
    # 번역기 초기화
    translator = Translator()

    # 현재 폴더를 기준으로 파일 경로 설정
    input_path = "./" + input_file
    output_path = "./" + output_file

    # 영어 문서 읽기
    with open(input_path, 'r', encoding='utf-8') as file:
        english_text = file.read()

    # 영어를 한국어로 번역
    korean_text = translator.translate(english_text, src='en', dest='ko').text

    # 번역된 내용을 파일에 저장
    with open(output_path, 'w', encoding='utf-8') as file:
        file.write(korean_text)

# 파일명을 적절히 수정하여 사용
translate_file("영어문서.txt", "한글번역.txt")