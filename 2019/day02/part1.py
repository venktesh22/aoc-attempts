from utils.file_io import read_input
from utils.timer import timer  # Importing the timer wrapper
import os

@timer
def solve_part1(input_data, debug=False):
    """
    Solves Part 1 of the puzzle.

    Args:
        input_data (str): The raw input data as a string.

    Returns:
        Any: The solution to Part 1.
    """
    # Add your solution logic here
    num_list = [int(s.strip()) for s in input_data.split(',')]
    num_list[1] = 12
    num_list[2] = 2

    cur_num = num_list[0]
    i = 0;

    while cur_num != 99:
        if cur_num == 1:
            num_list[num_list[i+3]] = num_list[num_list[i+1]] + num_list[num_list[i+2]]
            i += 4
            if debug:
                print(num_list)
        elif cur_num == 2:
            num_list[num_list[i+3]] = num_list[num_list[i+1]] * num_list[num_list[i+2]]
            i += 4
            if debug:
                print(num_list)
        else:
            break;
        cur_num = num_list[i]
    
    return num_list[0]


if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))
    input_data = read_input("input.txt", base_path=script_dir)
    print("Solution to Part 1:", solve_part1(input_data, True))
