from utils.file_io import read_input
from utils.timer import timer  # Importing the timer wrapper
import os

def operator(c,x,y):
    if c=='+':
        return x+y
    elif c=='*':
        return x*y
    else:
        return int(str(x)+str(y))

@timer
def solve_part2(input_data):
    import re
    from itertools import product
    valid = 0
    for input in input_data.split('\n'):
        nums = list(map(int,re.findall(r'\d+',input)))
        output, *vals = nums
        for combination in product(['+','*','|'], repeat=len(vals)-1):
            sum_val = operator(combination[0],vals[0],vals[1])
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
