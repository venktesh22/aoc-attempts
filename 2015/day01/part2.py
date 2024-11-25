from utils.file_io import read_input
from utils.timer import timer  # Importing the timer wrapper
import os

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
    cur_floor = 0
    pos = 1;
    for char in input_data:
        cur_floor += (1 if char == '(' else -1)
        if cur_floor < 0:
            return pos;
        pos += 1
    return None

if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))
    input_data = read_input("input.txt", base_path=script_dir)
    print("Solution to Part 1:", solve_part2(input_data))
