from hanspell import spell_checker
from pykospacing import Spacing

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

# 맞춤법 검사를 수행할 문장을 입력합니다.
sentence = input('문장을 입력하세요: ')
checked_sentence = correct_spelling(sentence)
print('검사 결과:', checked_sentence)