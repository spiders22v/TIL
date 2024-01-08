import os
from flask import Flask, render_template

PATH = r'34.플라스크 사진서버 만들기\static'

app = Flask(__name__)

@app.route('/')
def index():
    photos = os.listdir(PATH)
    return render_template('index2.html', photos=photos)

if __name__ == '__main__':
    app.run()
