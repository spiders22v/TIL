from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
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

    return render_template('index.html', questions=questions)

@app.route('/result', methods=['POST'])
def result():
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
        "ESFP": [1, 4, 6, 7, 10],
        "ENFP": [1, 2, 5, 6, 10],
        "ENTP": [3, 5, 7, 8, 10],
        "ESTJ": [1, 3, 8, 9, 10],
        "ESFJ": [1, 2, 6, 7, 10],
        "ENFJ": [2, 3, 5, 6, 7],
        "ENTJ": [3, 4, 5, 8, 9]
    }

    scores = { "E": 0, "I": 0, "S": 0, "N": 0, "T": 0, "F": 0, "J": 0, "P": 0 }

    for i in range(1, 11):
        answer = int(request.form['q' + str(i)])
        for k, v in results.items():
            if i in v:
                if answer <= 3:
                    scores[k[0]] += 1
                else:
                    scores[k[1]] += 1

    result = ""
    if scores['E'] > scores['I']:
        result += "E"
    else:
        result += "I"
    if scores['S'] > scores['N']:
        result += "S"
    else:
        result += "N"
    if scores['T'] > scores['F']:
        result += "T"
    else:
        result += "F"
    if scores['J'] > scores['P']:
        result += "J"
    else:
        result += "P"

    return render_template('result.html', result=result)

if __name__ == '__main__':
    app.run()
