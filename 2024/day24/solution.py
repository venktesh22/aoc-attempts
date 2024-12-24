import re
import numpy as np
from collections import Counter
from itertools import accumulate, product, permutations, combinations
from utils.file_io import read_input
from utils.timer import timer
import os

@timer
def solve_part1(input_data):
    codes, commands = input_data.split("\n\n")
    WIRE_TO_NUM = {}
    ALL_WIRES = set()
    for row in codes.split("\n"):
        a, b = row.split(":")
        b = int(b.strip())
        WIRE_TO_NUM[a] = b
        ALL_WIRES.add(a)
    
    all_list_by_output = {}
    for row in commands.split("\n"):
        by_space = row.split(" ")
        all_list_by_output[by_space[4]] = [by_space[0], by_space[1], by_space[2]]
        ALL_WIRES.add(by_space[0])
        ALL_WIRES.add(by_space[2])
        ALL_WIRES.add(by_space[4])
    
    while len(WIRE_TO_NUM) < len(ALL_WIRES):
        print(f"{len(WIRE_TO_NUM)}/{len(ALL_WIRES)} signals have outputs.")
        for out, inp in all_list_by_output.items():
            if (out not in WIRE_TO_NUM) and (inp[0] in WIRE_TO_NUM) and (inp[2] in WIRE_TO_NUM):
                match inp[1]:
                    case "XOR":
                        WIRE_TO_NUM[out] = WIRE_TO_NUM[inp[0]] ^ WIRE_TO_NUM[inp[2]]
                    case "OR":
                        WIRE_TO_NUM[out] = WIRE_TO_NUM[inp[0]] | WIRE_TO_NUM[inp[2]]
                    case "AND":
                        WIRE_TO_NUM[out] = WIRE_TO_NUM[inp[0]] & WIRE_TO_NUM[inp[2]]
                    case "_":
                        print(f"Not found...{by_space[1]}. Terminate")
        
    output = 0
    for wire, num in WIRE_TO_NUM.items():
        if wire.startswith('z') and num>0:
            output += num* (2**int(wire[1:]))
    return output

@timer
def solve_part2(input_data):
    """
    Incomplete attempt! It is a hard one. Combinatorial brute-force will fail.
    """
    codes, commands = input_data.split("\n\n")
    WIRE_TO_NUM = {}
    ALL_WIRES = set()
    for row in codes.split("\n"):
        a, b = row.split(":")
        b = int(b.strip())
        WIRE_TO_NUM[a] = b
        ALL_WIRES.add(a)
    x_output = 0 
    y_output = 0
    for wire, num in WIRE_TO_NUM.items():
        if wire.startswith('x') and num>0:
            x_output += num* (2**int(wire[1:]))
        if wire.startswith('y') and num>0:
            y_output += num* (2**int(wire[1:]))
    print(x_output,y_output)
    z = x_output+y_output
    print(f'Desired z={z}, with binary={bin(z)}')
    return None

if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))
    input_data = read_input("input.txt", base_path=script_dir)
    print("Solution to Part 1:", solve_part1(input_data))
    print("Solution to Part 2:", solve_part2(input_data))
