from utils.file_io import read_input
from utils.timer import timer  # Importing the timer wrapper
import os

@timer
def solve_part2(input_data):
    sum_val = 0
    all_rows = [row for row in input_data.split('\n')]
    from collections import Counter
    for i in range(0,len(all_rows),3):
        common = ''.join(set(all_rows[i]).intersection(all_rows[i+1], all_rows[i+2]))
        if common.isupper():
            sum_val += ord(common)-65+27
        else:
            sum_val += ord(common)-97+1
    return sum_val

if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))
    input_data = read_input("input.txt", base_path=script_dir)
    print("Solution to Part 2:", solve_part2(input_data))
