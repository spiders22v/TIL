from flask import Flask, render_template, request

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
    return render_template('index.html', candidates=candidates)

@app.route('/vote', methods=['POST'])
def vote():
    candidate = request.form['candidate']
    votes[candidate] += 1
    return "Vote cast for " + candidates[candidate]

if __name__ == '__main__':
    app.run()
