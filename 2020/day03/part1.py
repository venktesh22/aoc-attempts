from utils.file_io import read_input
from utils.timer import timer  # Importing the timer wrapper
import os

@timer
def solve_part1(input_data):
    char_list = [row for row in input_data.split('\n')]
    from itertools import cycle
    col_idx = cycle(range(len(char_list[0])))
    a = next(col_idx)
    num_trees = 0
    for row_idx in range(1,len(char_list)):
        a = [next(col_idx) for i in range(3)]
        eval_row, eval_col = row_idx, a[2]
        # print(eval_row, eval_col, char_list[eval_row][eval_col])
        if char_list[eval_row][eval_col]=='#':
            num_trees += 1
    
    return num_trees

if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))
    input_data = read_input("input.txt", base_path=script_dir)
    print("Solution to Part 1:", solve_part1(input_data))
