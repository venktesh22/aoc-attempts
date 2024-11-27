from utils.file_io import read_input
from utils.timer import timer  # Importing the timer wrapper
import os
from collections import Counter

@timer
def solve_part1(input_data):
    """
    Solves Part 1 of the puzzle.
    Rough logic is--> swap the string by zipping characters, then find

    Args:
        input_data (str): The raw input data as a string.

    Returns:
        Any: The solution to Part 1.
    """
    row_string_list = input_data.split('\n')
    columnintlist_list = list(zip(*row_string_list)) #first swap columns as rows
    index = 0
    gamma, epsilon = 0, 0
    for l in reversed(columnintlist_list):
        numbers = list(map(int,l)) #convert #s to int
        c = Counter(numbers)
        highest = c.most_common(1)[0][0]
        lowest = c.most_common(2)[1][0]
        gamma += (highest* 2**index)
        epsilon += (lowest * 2**index)
        index+= 1
        # print(numbers, gamma, epsilon)
    return gamma*epsilon


if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))
    input_data = read_input("input.txt", base_path=script_dir)
    print("Solution to Part 1:", solve_part1(input_data))
