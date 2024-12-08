from utils.file_io import read_input
from utils.timer import timer  # Importing the timer wrapper
import os

def operator(c,a,b):
    if c=='+':
        return a+b
    elif c=='*':
        return a*b
    else:
        # the ifs below can result in some speedup than int(str(a)+str(b))
        if (b < 10):
            return a * 10 + b
        if (b < 100):
            return a * 100 + b
        if (b < 1000):
            return a * 1000 + b
        if (b < 10000):
            return a * 10000 + b
        # return int(str(a)+str(b))

@timer
def solve_part2(input_data):
    import re
    from itertools import product
    valid = 0
    for input in input_data.split('\n'):
        nums = list(map(int,re.findall(r'\d+',input)))
        output, *vals = nums
        # already_explored_pattern_dict = {}
        for combination in product(['+','*','|'], repeat=len(vals)-1):
            sum_val = operator(combination[0],vals[0],vals[1])
            # if combination[0] not in already_explored_pattern_dict:
            #     already_explored_pattern_dict[combination[0]] = sum_val
            for i in range(1,len(combination)):
                sum_val = operator(combination[i], sum_val, vals[i+1])
                if sum_val > output:
                    break #too big already so skip
            if sum_val == output:
                valid += output
                break
    return valid

if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))
    input_data = read_input("input.txt", base_path=script_dir)
    print("Solution to Part 2:", solve_part2(input_data))
