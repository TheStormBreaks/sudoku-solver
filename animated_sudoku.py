import time
import os

def print_sudoku(grid):
    os.system('cls' if os.name == 'nt' else 'clear')
    for row in grid:
        print(" ".join (str(num) if num != 0 else '.' for num in row))
    time.sleep(0.1)

def is_safe(grid, row, col, num):
    for x in range(9):
        if grid[row][x] == num:
            return False
    
    for x in range(9):
        if grid[x][col] == num:
            return False
        
    start_row = row - row % 3
    start_col = col - col % 3
    for i in range(3):
        for j in range(3):
            if grid[start_row + i][start_col + j] == num:
                return False
    return True

def solve_sudoku(grid):
    for row in range(9):
        for col in range(9):
            if grid[row][col] == 0:
                for num in range(1, 10):
                    if is_safe(grid, row, col, num):
                        grid[row][col] = num
                        print_sudoku(grid)
                        if solve_sudoku(grid):
                            return True
                        grid[row][col] = 0
                        print_sudoku(grid)
                return False
    return True

def get_user_input():
    print("Enter your sudoku grid row by row.")
    print("Use 0 for empty cells.")
    grid = []
    for i in range(9):
        while True:
            try:
                row = input(f"Enter the row {i + 1} ( 9 numbers seperated by spaces ): ").strip()
                row = list(map(int, row.split()))
                if len(row) == 9 and all (0 <= num <= 9 for num in row):
                    grid.append(row)
                    break
                else:
                    print("Invalid Input")
            except ValueError:
                print("Invalid Input")
    return grid

if __name__ == "__main__":
    print("Sudoku Solver")
    sudoku_grid = get_user_input()
    print("\nOriginal Grid: ")
    print_sudoku(sudoku_grid)

    if solve_sudoku(sudoku_grid):
        print("\nSolved Sudoku Grid: ")
        print_sudoku(sudoku_grid)
    else:
        print("\nNo solutions exists.")

