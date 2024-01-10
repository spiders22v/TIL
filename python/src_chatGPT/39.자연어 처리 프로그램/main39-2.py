from konlpy.tag import Komoran

# Komoran 형태소 분석기 객체 생성
komoran = Komoran()

# 입력된 텍스트를 형태소 단위로 분석하고, 품사 태깅 수행
text = "오늘은 날씨가 좋아서 산책을 하고 싶습니다."
words = komoran.pos(text)

# 분석된 결과 출력
for word, pos in words:
    print(word, "(", pos, ")")
