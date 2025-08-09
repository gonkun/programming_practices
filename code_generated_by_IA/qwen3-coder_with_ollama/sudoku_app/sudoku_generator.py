# sudoku_generator.py

import random

def is_valid(board, row, col, num):
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False

    start_row = (row // 3) * 3
    start_col = (col // 3) * 3
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if board[i][j] == num:
                return False
    return True

def solve_sudoku(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                for num in random.sample(range(1, 10), 9):  # Mezcla números del 1 al 9
                    if is_valid(board, row, col, num):
                        board[row][col] = num
                        if solve_sudoku(board):
                            return True
                        board[row][col] = 0
                return False
    return True

def generate_sudoku():
    board = [[0 for _ in range(9)] for _ in range(9)]
    solve_sudoku(board)

    # Elimina algunos números para hacerlo un juego
    puzzle = [row[:] for row in board]
    cells_to_remove = 40  # Ajusta según dificultad

    for _ in range(cells_to_remove):
        row, col = random.randint(0, 8), random.randint(0, 8)
        while puzzle[row][col] == 0:
            row, col = random.randint(0, 8), random.randint(0, 8)
        puzzle[row][col] = 0

    return puzzle