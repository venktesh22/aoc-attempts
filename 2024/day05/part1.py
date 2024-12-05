from utils.file_io import read_input
from utils.timer import timer  # Importing the timer wrapper
import os
import re
from collections import defaultdict, deque
import numpy as np

def parse_rules_v4(rules):
    after_before_dict = defaultdict(list)
    for rule in rules.split('\n'):
        before, after = map(int,rule.split("|"))
        after_before_dict[after].append(before)
    return after_before_dict

def evaluate_rules(int_list, after_before_dict):
    for i,num in enumerate(int_list):
        for j in range(i,len(int_list)):
            if int_list[j] in after_before_dict[num]:
                return False
    return True

@timer
def solve_part1(input_data):
    rules, updates = input_data.split("\n\n")
    after_before_dict = parse_rules_v4(rules)

    sum_num = 0
    for update in updates.split('\n'):
        int_list = [int(n) for n in re.findall(r'\d+', update)]
        # if is_sublist_in_order(int_list,ordered_list_of_rules):
        if evaluate_rules(int_list,after_before_dict):
            sum_num += int_list[int(len(int_list)/2)]

    return sum_num

if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))
    input_data = read_input("input.txt", base_path=script_dir)
    print("Solution to Part 1:", solve_part1(input_data))
