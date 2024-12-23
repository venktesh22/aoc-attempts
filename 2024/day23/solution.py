import re
import numpy as np
from collections import Counter
from itertools import accumulate, product, permutations, combinations
from utils.file_io import read_input
from utils.timer import timer
import os
import networkx as nx

@timer
def solve_part1(input_data):
    G = nx.Graph()
    for line in input_data.split("\n"):
        n1, n2 = line.split("-")
        G.add_edge(n1,n2)
    count = 0
    for c in nx.enumerate_all_cliques(G):
        if len(c) < 3:
            continue
        elif len(c) > 3:
            break
        if any(n.startswith('t') for n in c):
            # print("t found in clique", c, "count=",count)
            count += 1
    return count

@timer
def solve_part2(input_data):
    G = nx.Graph()
    for line in input_data.split("\n"):
        n1, n2 = line.split("-")
        G.add_edge(n1,n2)
    cliques = list(nx.enumerate_all_cliques(G))  # Collect all cliques into a list
    sorted_lst = sorted(cliques[-1], key=lambda x: (x[0], x[1]))
    # print(sorted_lst)
    return ",".join(sorted_lst)

if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))
    input_data = read_input("input.txt", base_path=script_dir)
    print("Solution to Part 1:", solve_part1(input_data))
    print("Solution to Part 2:", solve_part2(input_data))
