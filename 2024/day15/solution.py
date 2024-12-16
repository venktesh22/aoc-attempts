import re
import numpy as np
from collections import Counter
from itertools import accumulate, product, permutations, combinations
from utils.file_io import read_input
from utils.timer import timer
import os

def pretty_print_grids(grid1):
    for row1 in grid1:
        print("".join(k for k in row1))
    print('\n')

def update_grid(grid, output, fish_pos, move):
    if move == "\n":
        return grid, output, fish_pos
    moves = {
        '>': (0,  1,   1),
        '<': (0, -1,   1),
        'v': (1,  0, 100),
        '^': (-1, 0, 100)
    }

    dx, dy, multiplier = moves[move]
    x, y = fish_pos
    nx, ny = x + dx, y + dy

    if grid[nx][ny] == "O":
        # Find how many continuous "O"s
        k = 1
        while True:
            k += 1
            if grid[x + dx*k][y + dy*k] != "O":
                break
        # Now grid[x + dx*k][y + dy*k] is the cell after the chain of "O"s
        if grid[x + dx*k][y + dy*k] == ".":
            # Move the O chain
            grid[x + dx*k][y + dy*k] = "O"
            grid[nx][ny] = "@"
            grid[x][y] = "."
            fish_pos = [x + dx, y + dy]
            # Adjust output by (k-1) * multiplier. Positive if moving down/right, negative if up/left.
            # We detect sign from dx, dy
            # For horizontal moves: move ">" increments output, "<" decrements; similarly for vertical.
            sign = 1 if (dy > 0 or dx > 0) else -1
            output += sign * (k - 1) * multiplier
    elif grid[nx][ny] == ".":
        # Just move fish
        grid[nx][ny] = "@"
        grid[x][y] = "."
        fish_pos = [nx, ny]

    return grid, output, fish_pos

@timer
def solve_part1(input_data):
    grid, moves = input_data.split("\n\n")
    grid = [[k for k in row] for row in grid.split("\n")]
    fish_pos =  next([r, c] for r, row in enumerate(grid) for c, col in enumerate(row) if col == "@")
    output = sum(100*r+c for r, row in enumerate(grid) for c, col in enumerate(row) if col == "O")
    for move in moves:
        # pretty_print_grids(grid)
        # print("Applying move", move)
        grid, output, fish_pos = update_grid(grid, output, fish_pos, move)
    pretty_print_grids(grid)
    output2 = sum(100*r+c for r, row in enumerate(grid) for c, col in enumerate(row) if col == "O")
    print(fish_pos, output, output2)
    return None

@timer
def solve_part2(input_data):
    input_data = """#######
#...#.#
#.....#
#..OO@#
#..O..#
#.....#
#######

<vv<<^^<<^^"""
    grid, moves = input_data.split("\n\n")
    actual_grid = grid.split("\n")
    for i, row in enumerate(actual_grid):
        row = row.replace('#', '##')
        row = row.replace('O', '[]')
        row = row.replace('.', '..')
        row = row.replace('@','@.')
        actual_grid[i] = row
    grid = [[k for k in row] for row in actual_grid]
    pretty_print_grids(grid)
    #I give up for now; perhaps will try later!
    return None

if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))
    input_data = read_input("input.txt", base_path=script_dir)
    print("Solution to Part 1:", solve_part1(input_data))
    print("Solution to Part 2:", solve_part2(input_data))
