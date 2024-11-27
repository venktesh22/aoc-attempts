from utils.file_io import read_input
from utils.timer import timer  # Importing the timer wrapper
import os
import numpy as np
from collections import Counter

@timer
def solve_part1(input_data):
    """
    Solves Part 1 of the puzzle.

    Args:
        input_data (str): The raw input data as a string.

    Returns:
        Any: The solution to Part 1.
    """
    num_list = np.array([int(s.strip()) for s in input_data.split('\n')])
    diff_list = num_list[1:] - num_list[:-1]
    inc_count = sum(1 for x in diff_list if x > 0)
    return inc_count

if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))
    input_data = read_input("input.txt", base_path=script_dir)
    print("Solution to Part 1:", solve_part1(input_data))
