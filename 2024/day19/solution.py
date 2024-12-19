import re
import numpy as np
from collections import Counter
from functools import cache, lru_cache
from itertools import accumulate, product, permutations, combinations
from utils.file_io import read_input
from utils.timer import timer
import os


@timer
def solve_part1(input_data):
    valid_p, designs = input_data.split("\n\n")
    available_patterns = list(map(str.strip, valid_p.split(",")))
    designs = list(map(str.strip, designs.split("\n")))
    # print(available_patterns, designs)
    @lru_cache
    def is_design_possible(design):
        if not design:
            return True #empty pattern
        results = []
        for pattern in available_patterns:
            if design.startswith(pattern):
                remainder = design[len(pattern):]
                results.append(is_design_possible(remainder))
        return any(results)
    count = sum([1 for design in designs if is_design_possible(design)])

    return count

@timer
def solve_part2(input_data):
    valid_p, designs = input_data.split("\n\n")
    available_patterns = list(map(str.strip, valid_p.split(",")))
    designs = list(map(str.strip, designs.split("\n")))
    # print(available_patterns, designs)
    @lru_cache
    def num_design_possible(design):
        if not design:
            return 1 #empty pattern
        results = []
        for pattern in available_patterns:
            if design.startswith(pattern):
                remainder = design[len(pattern):]
                results.append(num_design_possible(remainder))
        return sum(results)
    count = sum([num_design_possible(design) for design in designs])

    return count

if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))
    input_data = read_input("input.txt", base_path=script_dir)
    print("Solution to Part 1:", solve_part1(input_data))
    print("Solution to Part 2:", solve_part2(input_data))
