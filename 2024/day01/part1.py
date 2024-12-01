from utils.file_io import read_input
from utils.timer import timer  # Importing the timer wrapper
import os

@timer
def solve_part1(input_data):
    list1, list2 = [], []
    for row in input_data.split('\n'):
        list1.append(int(row.split()[0]))
        list2.append(int(row.split()[1]))
    list1, list2 = sorted(list1), sorted(list2)
    ans = 0
    for a,b in zip(list1, list2):
        ans += abs(a-b)
    return ans

if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))
    input_data = read_input("input.txt", base_path=script_dir)
    print("Solution to Part 1:", solve_part1(input_data))
