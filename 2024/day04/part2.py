from utils.file_io import read_input
from utils.timer import timer  # Importing the timer wrapper
import os

@timer
def solve_part2(input_data):
    grid = input_data.split('\n')
    rows = len(grid)
    cols = len(grid[0])

    def is_valid(x, y):
        return 0 <= x < rows and 0 <= y < cols

    def found_two_X_MAS(x, y):
        count_diag = 0
        # Top-left to bottom-right
        if is_valid(x - 1, y - 1) and is_valid(x + 1, y + 1):
            if grid[x - 1][y - 1] == "M" and grid[x + 1][y + 1] == "S":
                count_diag += 1

        # Top-right to bottom-left
        if is_valid(x - 1, y + 1) and is_valid(x + 1, y - 1):
            if grid[x - 1][y + 1] == "M" and grid[x + 1][y - 1] == "S":
                count_diag += 1

        # Bottom-left to top-right
        if is_valid(x + 1, y - 1) and is_valid(x - 1, y + 1):
            if grid[x + 1][y - 1] == "M" and grid[x - 1][y + 1] == "S":
                count_diag += 1

        # Bottom-right to top-left
        if is_valid(x + 1, y + 1) and is_valid(x - 1, y - 1):
            if grid[x + 1][y + 1] == "M" and grid[x - 1][y - 1] == "S":
                count_diag += 1

        return (count_diag==2)        

    count = 0
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == "A":  # Look for the center of the cross
                if found_two_X_MAS(i, j):
                    count += 1

    return count

if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))
    input_data = read_input("input.txt", base_path=script_dir)
    print("Solution to Part 2:", solve_part2(input_data))
