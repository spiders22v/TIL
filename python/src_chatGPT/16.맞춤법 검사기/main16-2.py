from hanspell import spell_checker
from pykospacing import Spacing

# 맞춤법 검사를 수행할 파일 경로를 지정합니다.
input_path = "16.맞춤법 검사기\틀린맞춤법.txt"
# 수정된 맞춤법을 저장할 파일 경로를 지정합니다.
output_path = "16.맞춤법 검사기\수정맞춤법.txt"

# 맞춤법 검사를 수행하는 함수를 정의합니다.
def correct_spelling(text):
    # PyKoSpacing 라이브러리를 사용하여 띄어쓰기를 보정합니다.
    spacing = Spacing()
    text = spacing(text)
    # hanspell 라이브러리를 사용하여 맞춤법을 교정합니다.
    spelled_sent = spell_checker.check(text)
    # 교정된 문장을 반환합니다.
    corrected_sent = spelled_sent.checked
    return corrected_sent

# 입력 파일을 읽어서 맞춤법을 보정한 뒤 출력 파일에 저장합니다.
with open(input_path, "r", encoding="utf-8") as f:
    text = f.read()
    corrected_text = correct_spelling(text)

with open(output_path, "w", encoding="utf-8") as f:
    f.write(corrected_text)

print(f"맞춤법 검사가 완료되었습니다. 수정된 파일은 {output_path}에 저장되었습니다.")
