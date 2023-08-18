# app.py
from flask import Flask, render_template, request
from analysis import analyze_data

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.form['data']
    result = analyze_data(data)
    return render_template('result.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
