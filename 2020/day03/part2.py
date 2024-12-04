from utils.file_io import read_input
from utils.timer import timer  # Importing the timer wrapper
import os

def step_trees(row_step, col_step, char_list):
    from itertools import cycle
    col_idx = cycle(range(1,len(char_list[0])+1))
    a = next(col_idx)
    num_trees = 0
    for row_idx in range(row_step,len(char_list), row_step):
        a = [next(col_idx)-1 for i in range(col_step)]
        eval_row, eval_col = row_idx, a[col_step-1]
        if char_list[eval_row][eval_col]=='#':
            num_trees += 1
    return num_trees

@timer
def solve_part2(input_data):
    char_list = [row for row in input_data.split('\n')]
    import numpy
    mul_trees = numpy.prod([step_trees(a,b,char_list) for a, b in zip([1,1,1,1,2],[1,3,5,7,1])])
    # print(mul_trees)
    return mul_trees
    

if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))
    input_data = read_input("input.txt", base_path=script_dir)
    print("Solution to Part 2:", solve_part2(input_data))
