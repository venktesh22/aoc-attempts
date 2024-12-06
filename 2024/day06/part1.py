from utils.file_io import read_input
from utils.timer import timer  # Importing the timer wrapper
import os
import re


@timer
def solve_part1(input_data):
    grid = [list(row) for row in input_data.split('\n')]
    rows, cols = len(grid), len(grid[0])
    for y, row in enumerate(grid):
        if '^' in row:
            start_y, start_x = y, row.index('^')
    x ,y, direction = start_x, start_y, '^'

    def is_valid(x, y):
        return 0 <= x < cols and 0 <= y < rows
    
    move = { "^": (0,-1),  ">": (1,0),  "v": (0,1),  "<": (-1,0) }
    ninety_degree = {"^":">", ">":"v", "v":"<", "<":"^"}

    while is_valid(x,y):
        dx,dy = move[direction]
        if not is_valid(x+dx,y+dy):
            grid[y][x] = 'X'
            break
        if grid[y+dy][x+dx] == '#':
            direction = ninety_degree[direction]
        else:
            grid[y][x] = 'X'
            x ,y = x+dx, y+dy
    
    return sum(1 for i in range(rows) for j in range(cols) if grid[i][j] == 'X')

if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))
    input_data = read_input("input.txt", base_path=script_dir)
    print("Solution to Part 1:", solve_part1(input_data))
