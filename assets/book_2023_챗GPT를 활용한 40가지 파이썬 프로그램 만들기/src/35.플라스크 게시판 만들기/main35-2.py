from flask import Flask, render_template, request, redirect, url_for
import os

PATH = r"35.플라스크 게시판 만들기\messages.txt"

app = Flask(__name__)

# 데이터를 저장할 리스트
messages = []

@app.route('/', methods=['GET', 'POST'])
def home():
    # 함수 내부에서 messages 변수를 사용하기 위해 global 키워드를 사용합니다.
    global messages
    if request.method == 'POST':
        # 게시물 작성을 요청한 경우
        message = request.form.get('message')
        messages.append(message)
        # 파일에 게시물 내용 저장
        with open(PATH, 'a') as f:
            f.write(message + '\n')
        return redirect(url_for('home'))
    else:
        # 저장된 게시물 내용 로드
        if os.path.exists(PATH):
            with open(PATH, 'r') as f:
                messages = [line.strip() for line in f.readlines()]
        # 게시물 목록을 보여줍니다.
        return render_template('index.html', messages=messages)

if __name__ == '__main__':
    app.run(debug=True)
