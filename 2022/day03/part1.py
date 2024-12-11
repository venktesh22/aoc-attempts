from utils.file_io import read_input
from utils.timer import timer  # Importing the timer wrapper
import os

@timer
def solve_part1(input_data):
    sum_val = 0
    for row in input_data.split('\n'):
        part1, part2 = row[:int(len(row)/2)], row[int(len(row)/2):]
        common = ''.join(set(part1).intersection(part2))
        if common.isupper():
            sum_val += ord(common)-65+27
        else:
            sum_val += ord(common)-97+1
    return sum_val

if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))
    input_data = read_input("input.txt", base_path=script_dir)
    print("Solution to Part 1:", solve_part1(input_data))
