from utils.file_io import read_input
from utils.timer import timer  # Importing the timer wrapper
import os

@timer
def solve_part1(input_data):
    grid = input_data.split('\n')
    target = "XMAS"
    rows = len(grid)
    cols = len(grid[0])

    def is_valid(x, y):
        return 0 <= x < rows and 0 <= y < cols

    def search_from(x, y, direction):
        dx, dy = direction
        for i in range(len(target)):
            nx, ny = x + i * dx, y + i * dy
            if not is_valid(nx, ny):
                return False
            if grid[nx][ny] != target[i]:
                return False
        return True
    count = 0
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == target[0]:  # First character matches
                for direction in [(0, 1),(0, -1),(1, 0),(-1, 0),(1, 1),(1, -1),(-1, 1),(-1, -1)]:
                    if search_from(i, j, direction):
                        count += 1 

    return count

if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))
    input_data = read_input("input.txt", base_path=script_dir)
    print("Solution to Part 1:", solve_part1(input_data))
