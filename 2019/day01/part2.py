from utils.file_io import read_input
from utils.timer import timer  # Importing the timer wrapper
import os

def func(x):
    if x <=6:
        return 0;
    else:
        return func(int(x/3)-2) + int(x/3)-2

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
    return sum(func(int(s.strip())) for s in input_data.split('\n'))

if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))
    input_data = read_input("input.txt", base_path=script_dir)
    print("Solution to Part 2:", solve_part2(input_data))
