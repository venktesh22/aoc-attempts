from utils.file_io import read_input
from utils.timer import timer  # Importing the timer wrapper
import os

@timer
def solve_part2(input_data):
    import re
    import numpy as np
    array = np.zeros((1000, 1000))
    for row in input_data.split("\n"):
        number = list(map(int, re.findall(r'\d+', row)))
        if number[0]==number[2] and number[1]!=number[3]:
            for i in range(min(number[1], number[3]), max(number[1], number[3])+1):
                array[number[0],i] += 1
        elif number[1]==number[3] and number[0]!=number[2]:
            for i in range(min(number[0], number[2]), max(number[0], number[2])+1):
                array[i,number[1]] += 1
        else:
            slope = (number[3]-number[1])/(number[2]-number[0])
            if slope>0:
                #run for equal increments
                for i in range(abs(number[3]-number[1])+1):
                    array[min(number[0], number[2])+i,min(number[1], number[3])+i] += 1
            else:
                p = 1 if number[1] > number[3] else -1
                for i in range(0, number[1]-number[3] + p, p):
                    array[number[0]+i, number[1]-i] += 1
    # print(array)
    answer = sum([sum([1 if k >= 2 else 0 for k in r]) for r in array])
    # print(answer)

    return answer

if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))
    input_data = read_input("input.txt", base_path=script_dir)
    print("Solution to Part 2:", solve_part2(input_data))
