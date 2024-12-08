from utils.file_io import read_input
from utils.timer import timer  # Importing the timer wrapper
import os
from collections import Counter
from itertools import combinations

def pretty_print_grid(grid):
    for row in grid:
        print(' '.join(row))
    print('\n')

@timer
def solve_part1(input_data):
    grid = input_data.split('\n')
    rows, cols = len(grid), len(grid[0])
    is_valid = lambda x, y: 0 <= x < cols and 0 <= y < rows
    antinode_grid = [['.' for _ in range(cols)] for _ in range(rows)]
    all_chars = Counter(input_data) #find all unique characters

    for char, _ in all_chars.items():
        if char in ['.', '\n']:
            continue
        #get unique character's coordinate in the grid
        all_coords = [(x, y) for y, row in enumerate(grid) for x, c in enumerate(row) if c == char]
        for (x1, y1), (x2, y2) in combinations(all_coords, 2):
            for (nx, ny) in [(x2 + (x2 - x1), y2 + (y2 - y1)), (x1 - (x2 - x1), y1 - (y2 - y1))]:
                if is_valid(nx, ny):
                    antinode_grid[ny][nx] = '#'

    return sum(c == '#' for row in antinode_grid for c in row)

if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))
    input_data = read_input("input.txt", base_path=script_dir)
    print("Solution to Part 1:", solve_part1(input_data))
