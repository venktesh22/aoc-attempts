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
    ans = 0
    for i in range(len(input_data)):
        if i< len(input_data)-1:
            if input_data[i]==input_data[i+1]:
                ans += int(input_data[i])
        else:
            if input_data[i]==input_data[0]:
                ans += int(input_data[i])
    # Add your solution logic here
    return ans

if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))
    input_data = read_input("input.txt", base_path=script_dir)
    print("Solution to Part 1:", solve_part1(input_data))
