from utils.file_io import read_input
from utils.timer import timer  # Importing the timer wrapper
import os
import re

@timer
def solve_part1(input_data):
    """
    Solves Part 1 of the puzzle.

    Args:
        input_data (str): The raw input data as a string.

    Returns:
        Any: The solution to Part 1.
    """
    # Add your solution logic here
    sum_val = 0
    for line in input_data.split("\n"):
        # print(line)
        total_area = lambda dim: (lambda l, w, h: 2*(l*w + w*h + h*l) + min(l*w, w*h, h*l))(*map(int, re.split(r'x', dim)))
        sum_val += total_area(line)
        # break
    print(sum_val)
    return sum_val

if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))
    input_data = read_input("input.txt", base_path=script_dir)
    print("Solution to Part 1:", solve_part1(input_data))
