from utils.file_io import read_input
from utils.timer import timer  # Importing the timer wrapper
import os
import re
from collections import defaultdict, deque
import numpy as np
from itertools import permutations

def parse_rules_v4(rules):
    after_before_dict = defaultdict(list)
    for rule in rules.split('\n'):
        before, after = map(int,rule.split("|"))
        after_before_dict[after].append(before)
    return after_before_dict

def evaluate_rules(int_list, after_before_dict):
    flag = True
    # print('Evaluating list',int_list)
    for i,after_num in enumerate(int_list):
        for j in range(i,len(int_list)):
            if int_list[j] in after_before_dict[after_num]:
                # print(f'Violation detected. {int_list[j]} should be before {after_num}.')
                flag = False
    return flag
    
def fix_int_list(int_list,after_before_dict):
    # print('Original list:', int_list)
    changed = True

    while changed:
        changed = False
        for i, after_num in enumerate(int_list):
            for j in range(i + 1, len(int_list)):
                # If there's a violation, move the violating element
                if int_list[j] in after_before_dict.get(after_num, []):
                    # print(f'Moving {int_list[j]} to before {after_num}')
                    # Move int_list[j] to position i, shifting others
                    violating_element = int_list.pop(j)
                    int_list.insert(i, violating_element)
                    changed = True
                    break
            if changed:
                break
    # print('Fixed list:', int_list)
    return int_list

@timer
def solve_part2(input_data):
    
    rules, updates = input_data.split("\n\n")
    after_before_dict = parse_rules_v4(rules)

    sum_num = 0
    i = 0
    for update in updates.split('\n'):
        int_list = [int(n) for n in re.findall(r'\d+', update)]
        if not evaluate_rules(int_list,after_before_dict):
            # print('Evaluating failed list',i)
            int_list = fix_int_list(int_list, after_before_dict)
            sum_num += int_list[int(len(int_list)/2)]
            i+=1
    return sum_num

if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))
    input_data = read_input("input.txt", base_path=script_dir)
    print("Solution to Part 2:", solve_part2(input_data))
