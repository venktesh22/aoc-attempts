from utils.file_io import read_input
from utils.timer import timer  # Importing the timer wrapper
import os

def get_num_fish(fish_num, num_days):
    #returns number of fishes with fish_num=0 reproduce to after num_days
    if num_days <= 0:
        return 1
    if fish_num > 0:
        return get_num_fish(fish_num-1, num_days-1)
    else:
        return get_num_fish(6, num_days-1)+get_num_fish(8, num_days-1)

@timer
def solve_part1(input_data):
    """
    Solves Part 1 of the puzzle.

    Args:
        input_data (str): The raw input data as a string.

    Returns:
        Any: The solution to Part 1.
    """
    from collections import Counter
    all_nums = Counter([int(s.strip()) for s in input_data.split(",")])
    final_num_fish = 0
    for num in all_nums:
        final_num_fish += all_nums[num]*get_num_fish(num,80)
    print(final_num_fish)
    return final_num_fish

if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))
    input_data = read_input("input.txt", base_path=script_dir)
    print("Solution to Part 1:", solve_part1(input_data))
