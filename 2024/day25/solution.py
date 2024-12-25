import re
import numpy as np
from collections import Counter
from itertools import accumulate, product, permutations, combinations
from utils.file_io import read_input
from utils.timer import timer
import os

def count_hash_col(grid):
    out = [0 for _ in range(len(grid[0]))]
    for j in range(len(grid[0])):
        for i in range(len(grid)):
            if grid[i][j]=="#":
                out[j]+=1
    return out

@timer
def solve_part1(input_data):
    grids = input_data.split("\n\n")
    lockgrids = []
    keygrids = []
    for grid in grids:
        grid = [[s for s in row] for row in grid.split("\n")]
        if grid[0][0]=="#":
            lockgrids.append(count_hash_col(grid[1:]))
        else:
            keygrids.append(count_hash_col(grid[:-1]))
    numfits = 0
    for lock in lockgrids:
        for key in keygrids:
            sumlist = [x + y for x, y in zip(lock, key)]
            if all(x <= 5 for x in sumlist):
                numfits += 1

    return numfits

@timer
def solve_part2(input_data):
    """
    Solves Part 2 of the puzzle.

    Args:
        input_data (str): The raw input data as a string.

    Returns:
        Any: The solution to Part 2.
    """
    # Add your solution logic here
    return None

if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))
    input_data = read_input("input.txt", base_path=script_dir)
    print("Solution to Part 1:", solve_part1(input_data))
    print("Solution to Part 2:", solve_part2(input_data))
