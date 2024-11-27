from utils.file_io import read_input
from utils.timer import timer  # Importing the timer wrapper
import os
import numpy as np

@timer
def solve_part2(input_data):
    """
    Solves Part 2 of the puzzle.

    Args:
        input_data (str): The raw input data as a string.

    Returns:
        Any: The solution to Part 2.
    """
    num_list = np.array([int(s.strip()) for s in input_data.split('\n')])
    new_num_list = np.array([sum(num_list[k] for k in range(x,x+3)) for x in range(len(num_list)-2)])
    print(new_num_list)
    diff_list = new_num_list[1:] - new_num_list[:-1]
    inc_count = sum(1 for x in diff_list if x > 0)
    return inc_count

if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))
    input_data = read_input("input.txt", base_path=script_dir)
    print("Solution to Part 2:", solve_part2(input_data))
