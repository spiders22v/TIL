print("MBTI 성격유형검사")
print("각 문항에 대해 가장 적절한 답변을 선택해주세요.")
print("1: 전혀 그렇지 않다 / 2: 그렇지 않은 편이다 / 3: 보통이다 / 4: 그렇다 / 5: 매우 그렇다")

questions = [
    "1. 대체로 사람들과 어울리는 것을 좋아한다.",
    "2. 논쟁보다는 타협하는 것이 좋다고 생각한다.",
    "3. 대개 계획을 세우는 것을 좋아한다.",
    "4. 새로운 일에 도전하는 것을 좋아한다.",
    "5. 감정을 드러내는 것보다는 이성적으로 생각하는 것이 좋다고 생각한다.",
    "6. 대체로 조용한 분위기를 좋아한다.",
    "7. 사람들과의 대화에서 자주 말하는 편이다.",
    "8. 어떤 일을 할 때 체계적으로 처리하는 편이다.",
    "9. 강한 경쟁심이 있다.",
    "10. 주로 자신의 감정에 따라 일을 처리한다."
]

results = {
    "ISTJ": [1, 2, 3, 8, 10],
    "ISFJ": [1, 2, 3, 6, 10],
    "INFJ": [2, 3, 5, 6, 10],
    "INTJ": [3, 4, 5, 8, 10],
    "ISTP": [4, 6, 7, 9, 10],
    "ISFP": [4, 6, 7, 10],
    "INFP": [2, 5, 6, 10],
    "INTP": [3, 5, 6, 8, 10],
    "ESTP": [4, 6, 7, 9],
    "ESFP": [4, 6, 7],
    "ENFP": [2, 5, 6],
    "ENTP": [3, 5, 6, 9],
    "ESTJ": [1, 2, 3, 8, 9],
    "ESFJ": [1, 2, 3, 6, 9],
    "ENFJ": [2, 3, 5, 6, 9],
    "ENTJ": [3, 4, 5, 8, 9]
}

results_count = {result: 0 for result in results}

for i, question in enumerate(questions):
    print(question)
    while True:
        try:
            answer = int(input("답변을 입력해주세요: "))
            if answer < 1 or answer > 5:
                print("1에서 5 사이의 값을 입력해주세요.")
                continue
            break
        except ValueError:
            print("숫자를 입력해주세요.")

for result, result_answers in results.items():
    if i+1 in result_answers:
        results_count[result] += answer

max_result = max(results_count, key=results_count.get)
print(f"당신의 MBTI 성격유형은 {max_result}입니다.")
