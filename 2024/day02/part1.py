from utils.file_io import read_input
from utils.timer import timer  # Importing the timer wrapper
import os

@timer
def solve_part1(input_data):
    import re
    import numpy as np
    find_integers = re.compile(r'\d+').findall
    safe = 0
    for row in input_data.split('\n'):
        row_int = list(map(int,find_integers(row)))
        print(row_int)
        diff = np.diff(row_int)
        count_neg = sum([1 for n in diff if n < 0])
        count_pos = sum([1 for n in diff if n > 0])
        count_high_diff = sum([1 for n in diff if abs(n) > 3])
        if count_high_diff > 0:
            continue
        if (count_pos == 0 and count_neg == len(diff)) or (count_neg==0 and count_pos== len(diff)):
            safe += 1
    return safe

if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))
    input_data = read_input("input.txt", base_path=script_dir)
    print("Solution to Part 1:", solve_part1(input_data))
