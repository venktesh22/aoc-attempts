from utils.file_io import read_input
from utils.timer import timer  # Importing the timer wrapper
import os
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
    # Add your solution logic here
    valid_pass = 0
    for row in input_data.split('\n'):
        low_num, high_num, letter, password = list(map(int,row.split(" ")[0].split('-'))) + row.split(" ", 1)[1].split(': ')
        c = Counter(password)[letter]
        if low_num <= c <= high_num:
            valid_pass+=1
        # break
    return valid_pass

if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))
    input_data = read_input("input.txt", base_path=script_dir)
    print("Solution to Part 1:", solve_part1(input_data))
