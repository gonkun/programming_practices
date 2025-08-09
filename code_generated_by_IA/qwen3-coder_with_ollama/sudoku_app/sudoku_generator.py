
# sudoku_generator.py

import random
from typing import List, Optional

class SudokuGenerator:
    def __init__(self, size: int = 9):
        self.size = size
        self.board: List[List[int]] = [[0 for _ in range(size)] for _ in range(size)]
        self.solve_sudoku()

    def is_valid(self, row: int, col: int, num: int) -> bool:
        # Check row and column
        for i in range(self.size):
            if self.board[row][i] == num or self.board[i][col] == num:
                return False

        # Check 3x3 subgrid
        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(start_row, start_row + 3):
            for j in range(start_col, start_col + 3):
                if self.board[i][j] == num:
                    return False
        return True

    def find_empty_cell(self) -> Optional[tuple[int, int]]:
        for i in range(self.size):
            for j in range(self.size):
                if self.board[i][j] == 0:
                    return (i, j)
        return None

    def solve_sudoku(self) -> bool:
        empty_cell = self.find_empty_cell()
        if not empty_cell:
            return True  # Puzzle solved

        row, col = empty_cell
        nums = list(range(1, self.size + 1))
        random.shuffle(nums)

        for num in nums:
            if self.is_valid(row, col, num):
                self.board[row][col] = num
                if self.solve_sudoku():
                    return True
                self.board[row][col] = 0  # Backtrack
        return False

    def generate_puzzle(self, cells_to_remove: int) -> List[List[int]]:
        """
        Generates a puzzle by removing a certain number of cells from the solved board.
        """
        puzzle = [row[:] for row in self.board]
        
        # Ensure cells_to_remove is within a reasonable range
        cells_to_remove = max(0, min(cells_to_remove, self.size * self.size - 17)) # Keep at least 17 clues

        attempts = 0
        removed_count = 0
        while removed_count < cells_to_remove and attempts < self.size * self.size * 2:
            row, col = random.randint(0, self.size - 1), random.randint(0, self.size - 1)
            if puzzle[row][col] != 0:
                puzzle[row][col] = 0
                removed_count += 1
            attempts += 1
            
        return puzzle

if __name__ == '__main__':
    # Example of how to use the generator
    generator = SudokuGenerator()
    
    # Difficulty levels
    difficulties = {
        "easy": 35,
        "medium": 45,
        "hard": 55
    }

    for level, cells in difficulties.items():
        print(f"\n--- {level.capitalize()} Puzzle ---")
        puzzle = generator.generate_puzzle(cells)
        for row in puzzle:
            print(" ".join(str(num) if num != 0 else "." for num in row))
