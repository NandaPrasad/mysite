
# A very simple Flask Hello World app for you to get started with...

from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('main.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/results')
def results():
    return render_template('results.html')

