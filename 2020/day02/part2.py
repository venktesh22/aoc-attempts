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
    valid_pass = 0
    for row in input_data.split('\n'):
        low_num, high_num, letter, password = list(map(int,row.split(" ")[0].split('-'))) + row.split(" ", 1)[1].split(': ')
        # xor gate in python is bool(cond1) ^ bool(cond2)
        if bool(password[low_num-1]==letter) ^ bool(password[high_num-1]==letter):
            valid_pass+=1
        # break
    return valid_pass

if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))
    input_data = read_input("input.txt", base_path=script_dir)
    print("Solution to Part 2:", solve_part2(input_data))
