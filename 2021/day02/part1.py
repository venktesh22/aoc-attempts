from utils.file_io import read_input
from utils.timer import timer  # Importing the timer wrapper
import os

@timer
def solve_part1(input_data):
    """
    Solves Part 1 of the puzzle.

    Args:
        input_data (str): The raw input data as a string.

    Returns:
        Any: The solution to Part 1.
    """
    forw, depth = 0,0
    for row in input_data.split('\n'):
        direc, step = row.split(" ")
        forw += int(step) if direc == "forward" else 0
        if direc!="forward":
            depth += int(step)*(1 if direc=="down" else -1)
    return forw*depth

if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))
    input_data = read_input("input.txt", base_path=script_dir)
    print("Solution to Part 1:", solve_part1(input_data))
