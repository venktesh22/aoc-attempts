import re
import numpy as np
from collections import Counter, defaultdict
from itertools import accumulate, product, permutations, combinations
from utils.file_io import read_input
from utils.timer import timer
from functools import lru_cache
import os

import sys
np.set_printoptions(threshold=sys.maxsize)

def mix_prune(orig, mix):
    return (orig^mix)%16777216

@lru_cache
def get_new_secret(orig):
    orig = mix_prune(orig, orig*64)
    orig = mix_prune(orig, int(orig/32))
    orig = mix_prune(orig, orig*2048)
    return orig

@timer
def solve_part1(input_data):
    nums = list(map(int, input_data.split("\n")))
    for _ in range(2000):
        nums = [get_new_secret(n) for n in nums]
    return sum(nums)

@timer
def solve_part2(input_data):
    nums = list(map(int, input_data.split("\n")))
    last_digit_diff = []
    list_pattern_to_dict = []
    for n in nums:
        pattern_to_number = {} # Will map 4-diff-string -> integer
        k = n
        #use walrus operator to assign and repeat
        last_digit = [k % 10] + [(k := get_new_secret(k)) % 10 for _ in range(2000)]
        last_digit = np.array(last_digit)
        last_digit_diff = np.diff(last_digit)
        
        # Slide a window of size 4 through last_digit_diff, Extract the 4 consecutive diffs, 
        for i in range(len(last_digit_diff) - 4 + 1):
            window = last_digit_diff[i : i + 4]
            # Convert diff to a string; [-3, 6, -1, -1] => "-3,6,-1,-1"
            window_str = ",".join(str(x) for x in window)
            if window_str not in pattern_to_number:
                pattern_to_number[window_str] = last_digit[i + 4]
        list_pattern_to_dict.append(pattern_to_number)
    aggregate_dict = {}
    for d in list_pattern_to_dict:
        for pattern, val in d.items():
            #default to 0
            aggregate_dict[pattern] = aggregate_dict.get(pattern, 0) + val

    # Maximum value finder
    max_pattern = max(aggregate_dict, key=aggregate_dict.get)
    max_value = aggregate_dict[max_pattern]
    return max_value

if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))
    input_data = read_input("input.txt", base_path=script_dir)
    print("Solution to Part 1:", solve_part1(input_data))
    print("Solution to Part 2:", solve_part2(input_data))
