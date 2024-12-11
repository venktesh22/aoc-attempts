from utils.file_io import read_input
from utils.timer import timer  # Importing the timer wrapper
import os

@timer
def solve_part1(input_data):
    count =0
    for row in input_data.split('\n'):
        import re
        a1,a2,b1,b2 = map(int,re.findall(r'\d+',row))      
        if (a1>=b1 and a2<=b2) or (a1<=b1 and a2>=b2):
            count+=1
    return count

if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))
    input_data = read_input("input.txt", base_path=script_dir)
    print("Solution to Part 1:", solve_part1(input_data))
