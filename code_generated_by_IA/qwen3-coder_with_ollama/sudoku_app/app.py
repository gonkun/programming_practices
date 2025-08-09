# app.py

from flask import Flask, render_template
from sudoku_generator import generate_sudoku

app = Flask(__name__)

@app.route('/')
def index():
    puzzle = generate_sudoku()
    return render_template('index.html', puzzle=puzzle)

if __name__ == '__main__':
    app.run(debug=True)