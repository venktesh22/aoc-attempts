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
    import re
    import numpy as np
    array = np.zeros((1000, 1000))
    for row in input_data.split("\n"):
        number = list(map(int, re.findall(r'\d+', row)))
        if number[0]!=number[2] and number[1]!=number[3]:
            continue
        elif number[0]==number[2]:
            for i in range(min(number[1], number[3]), max(number[1], number[3])+1):
                array[number[0],i] += 1
        elif number[1]==number[3]:
            for i in range(min(number[0], number[2]), max(number[0], number[2])+1):
                array[i,number[1]] += 1
    print(array)
    answer = sum([sum([1 if k >= 2 else 0 for k in r]) for r in array])
    print(answer)

    return answer

if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))
    input_data = read_input("input.txt", base_path=script_dir)
    print("Solution to Part 1:", solve_part1(input_data))
