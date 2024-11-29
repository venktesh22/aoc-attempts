from utils.file_io import read_input
from utils.timer import timer  # Importing the timer wrapper
import os

@timer
def solve_part2(input_data):
    elf_data = input_data.split('\n\n');
    # print(elf_data)
    cal = []
    for elf in elf_data:
        cal.append(sum([int(s.strip()) for s in elf.split('\n')]))
    
    return sum(sorted(cal, reverse=True)[:3])

if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))
    input_data = read_input("input.txt", base_path=script_dir)
    print("Solution to Part 2:", solve_part2(input_data))
