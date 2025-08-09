
# app.py
from flask import Flask, render_template, request
from sudoku_generator import SudokuGenerator

app = Flask(__name__)

DIFFICULTY_LEVELS = {
    "easy": 35,
    "medium": 45,
    "hard": 55,
    "expert": 60
}

@app.route('/')
def index():
    difficulty = request.args.get('difficulty', 'medium').lower()
    if difficulty not in DIFFICULTY_LEVELS:
        difficulty = 'medium'
        
    cells_to_remove = DIFFICULTY_LEVELS[difficulty]
    
    # Create a new generator for each request to get a new puzzle
    sudoku_generator = SudokuGenerator()
    puzzle = sudoku_generator.generate_puzzle(cells_to_remove)
    
    return render_template(
        'index.html', 
        puzzle=puzzle, 
        levels=DIFFICULTY_LEVELS.keys(),
        current_difficulty=difficulty
    )

if __name__ == '__main__':
    app.run(debug=True)
