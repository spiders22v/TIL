from flask import Flask, render_template, request

app = Flask(__name__)

# 데이터를 저장할 리스트
messages = []

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        # 게시물 작성을 요청한 경우
        message = request.form.get('message')
        messages.append(message)
    # 게시물 목록을 보여줍니다.
    return render_template('index.html', messages=messages)

if __name__ == '__main__':
    app.run(debug=True)
