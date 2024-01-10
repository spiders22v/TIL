from flask import Flask, render_template
import matplotlib.pyplot as plt
import io
import base64

app = Flask(__name__)

candidates = {
    'candidate_1': 'Alice',
    'candidate_2': 'Bob',
    'candidate_3': 'Charlie'
}

votes = {
    'candidate_1': 0,
    'candidate_2': 0,
    'candidate_3': 0
}

@app.route('/')
def index():
    return render_template('index2.html', candidates=candidates)

@app.route('/vote/<candidate>')
def vote(candidate):
    votes[candidate] += 1
    return "Vote cast for " + candidates[candidate]

@app.route('/result')
def result():
    plt.bar(candidates.values(), votes.values())
    plt.title('Vote result')
    plt.xlabel('Candidate')
    plt.ylabel('Votes')
    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    graph_url = base64.b64encode(img.getvalue()).decode()
    return render_template('result.html', graph_url=graph_url)

if __name__ == '__main__':
    app.run()
