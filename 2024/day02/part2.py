from utils.file_io import read_input
from utils.timer import timer  # Importing the timer wrapper
import os
import numpy as np

def is_safe(row_int):
    diff = np.diff(row_int)
    count_neg = sum([1 for n in diff if n < 0])
    count_pos = sum([1 for n in diff if n > 0])
    count_high_diff = sum([1 for n in diff if abs(n) > 3])
    if count_high_diff > 0:
        return False
    if (count_pos == 0 and count_neg == len(diff)) or (count_neg==0 and count_pos== len(diff)):
        return True
    return False

@timer
def solve_part2(input_data):
    import re
    find_integers = re.compile(r'\d+').findall
    safe = 0
    unsafe_index = []
    for i, row in enumerate(input_data.split('\n')):
        row_int = list(map(int,find_integers(row)))
        if is_safe(row_int):
            safe+=1
        else:
            unsafe_index.append(i)
        
    data_split = input_data.split('\n')
    for i in unsafe_index:
        row_int = list(map(int,find_integers(data_split[i])))
        for index, element in enumerate(row_int):
            #check if removing j would make a list safe
            #note that elements may repeat, so we cannot just drop an element, but need to drop index
            temp_list = [element2 for k , element2 in enumerate(row_int) if k!=index]
            if is_safe(temp_list):
                safe+=1
                break

    return safe

if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))
    input_data = read_input("input.txt", base_path=script_dir)
    print("Solution to Part 2:", solve_part2(input_data))
