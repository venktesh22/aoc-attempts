from utils.file_io import read_input
from utils.timer import timer  # Importing the timer wrapper
import os

@timer
def solve_part2(input_data):
    list1, list2 = [], []
    for row in input_data.split('\n'):
        list1.append(int(row.split()[0]))
        list2.append(int(row.split()[1]))
    list1, list2 = sorted(list1), sorted(list2)
    from collections import Counter
    c1, c2 = Counter(list1), Counter(list2)
    sum =0
    for num in c1:
        if num in c2:
            sum+= c1[num]*num*c2[num]
    return sum

if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))
    input_data = read_input("input.txt", base_path=script_dir)
    print("Solution to Part 2:", solve_part2(input_data))
