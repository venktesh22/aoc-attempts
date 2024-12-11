import re
import numpy as np
from collections import Counter
from itertools import accumulate, product, permutations, combinations
from utils.file_io import read_input
from utils.timer import timer
import os
from functools import lru_cache

#function below failed for part 2 as it lead to increasing list sizes which was not required
# @lru_cache(maxsize=None)
# def analyze_stone(num, count):
#     num = num.strip()
#     if int(num)==0:
#         return analyze_stone(str(1), count-1) if count > 1 else [str(1)]
#     elif len(num)%2 == 0:
#         a = int(len(num)/2)
#         return analyze_stone(str(int(num[:a])), count-1) + analyze_stone(str(int(num[a:])), count-1) if count > 1 else [str(int(num[:a])), str(int(num[a:]))]
#     else:
#         return analyze_stone(str(int(num)*2024), count-1) if count > 1 else [str(int(num)*2024)]

@lru_cache(maxsize=None)
def count_num_stones(num, count):
    num = num.strip()
    if int(num)==0:
        return count_num_stones(str(1), count-1) if count > 1 else 1
    elif len(num)%2 == 0:
        a = int(len(num)/2)
        return count_num_stones(str(int(num[:a])), count-1) + count_num_stones(str(int(num[a:])), count-1) if count > 1 else 2
    else:
        return count_num_stones(str(int(num)*2024), count-1) if count > 1 else 1

@timer
def solve_part1(input_data):
    str_nums = input_data.split(" ")
    count_val = 0
    for num in str_nums:
        # count_val += len(analyze_stone(num,25))
        count_val += count_num_stones(num,25)

    return count_val

@timer
def solve_part2(input_data):
    str_nums = input_data.split(" ")
    count_val = 0
    for num in str_nums:
        # print("Analyzing num=", num)
        count_val += count_num_stones(num,75)
    return count_val

if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))
    input_data = read_input("input.txt", base_path=script_dir)
    print("Solution to Part 1:", solve_part1(input_data))
    print("Solution to Part 2:", solve_part2(input_data))
