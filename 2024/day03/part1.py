from utils.file_io import read_input
from utils.timer import timer  # Importing the timer wrapper
import os

@timer
def solve_part1(input_data):
    import re
    ans = sum(int(a) * int(b) for a, b in re.findall(r'mul\((\d+),(\d+)\)', input_data))
    return ans

if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))
    input_data = read_input("input.txt", base_path=script_dir)
    print("Solution to Part 1:", solve_part1(input_data))
