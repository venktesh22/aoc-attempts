import re
import numpy as np
from collections import Counter, deque
from itertools import accumulate, product, permutations, combinations
from utils.file_io import read_input
from utils.timer import timer
import os

def run_program(program,A,B,C):
    operand_dict = {0:0, 1:1, 2:2, 3:3, 4:A, 5:B, 6:C}
    pointer = 0
    output = []
    while pointer < len(program):
        operand_dict[4] = A
        operand_dict[5] = B
        operand_dict[6] = C 
        opcode, operand = program[pointer], program[pointer+1]
        # print(opcode, operand)
        match opcode:
            case 0:
                A = int(A/(2**operand_dict[operand]))
            case 1:
                B = B ^ operand
            case 2:
                B = operand_dict[operand] % 8
            case 3:
                if A != 0:
                    pointer = operand - 2 #operand_dict[operand]
            case 4:
                B = B^C
            case 5:
                output.append(operand_dict[operand] % 8)
            case 6:
                B = int(A/(2**operand_dict[operand]))
            case 7:
                C = int(A/(2**operand_dict[operand]))
        pointer += 2
        # print(f"Opcode={opcode}, Operand = {operand}, A={A},B={B},C={C}, and output={output}")
    return output

@timer
def solve_part1(input_data):

    registers, program = input_data.split("\n\n")
    A, B, C = list(map(int,re.findall(r'\d+', registers)))
    program = list(map(int,re.findall(r'\d+', program)))
    print(A,B,C,program)

    output = run_program(program,A,B,C)

    return (",".join(str(d) for d in output))

@timer
def solve_part2(input_data):
    registers, program = input_data.split("\n\n")
    A, B, C = list(map(int,re.findall(r'\d+', registers)))
    program = list(map(int,re.findall(r'\d+', program)))
    return None

if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))
    input_data = read_input("input.txt", base_path=script_dir)
    print("Solution to Part 1:", solve_part1(input_data))
    print("Solution to Part 2:", solve_part2(input_data))
