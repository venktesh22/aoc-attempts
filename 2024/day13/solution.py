import re
import numpy as np
from collections import Counter
from itertools import accumulate, product, permutations, combinations
from utils.file_io import read_input
from utils.timer import timer
import os
import math

def solve_equation(Ax, Ay, Bx, By, Tx, Ty):
    """
    Solve a system of two linear equation for p and q such that
    Ax*p+Bx*q = Tx
    Ay*p+By*q = Ty
    """
    tokens_needed = 0
    D = Ax * By - Bx * Ay # Calculate the determinant of the coefficient matrix
    if D != 0:
        #unique solution; Cramer rule
        Dp = Tx * By - Bx * Ty
        Dq = Ax * Ty - Tx * Ay
        p = Dp / D
        q = Dq / D
        fractional_p, int_p = math.modf(p)
        fractional_q, int_q = math.modf(q)
        
        if math.isclose(fractional_p, 0.0, abs_tol=1e-10) and math.isclose(fractional_q, 0.0, abs_tol=1e-10):
            tokens_needed = 3*int_p + int_q
    else:
        # It could be either dependent or inconsistent
        print("No unique solution")
    return tokens_needed

@timer
def solve_part1(input_data):
    tokens = 0
    for row in input_data.split('\n\n'):
        Ax, Ay, Bx, By, Tx, Ty = map(int,re.findall(r'\d+',row))
        tokens += solve_equation(Ax, Ay, Bx, By, Tx, Ty)
    return int(tokens)

@timer
def solve_part2(input_data):
    tokens = 0
    for row in input_data.split('\n\n'):
        Ax, Ay, Bx, By, Tx, Ty = map(int,re.findall(r'\d+',row))
        Tx += 10000000000000
        Ty += 10000000000000 
        tokens += solve_equation(Ax, Ay, Bx, By, Tx, Ty)
    return int(tokens)

if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))
    input_data = read_input("input.txt", base_path=script_dir)
    print("Solution to Part 1:", solve_part1(input_data))
    print("Solution to Part 2:", solve_part2(input_data))
