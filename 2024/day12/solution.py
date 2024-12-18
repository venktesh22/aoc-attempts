import re
import numpy as np
from collections import Counter
from itertools import accumulate, product, permutations, combinations
from utils.file_io import read_input
from utils.timer import timer
import os
import networkx as nx

def get_grid(input):
    grid = {}
    ncol = 0
    for i, row in enumerate(input.split("\n")):
        ncol = len(row)
        for j, col in enumerate(row):
            grid[i,j] = col
    return grid, len(input.split("\n")), ncol

def get_graph(grid, rows, cols):
    g = nx.Graph()
    directions = [(1,0),(0,1),(-1,0),(0,-1)]
    for r in range(rows):
        for c in range(cols):
            g.add_node((r, c))
            for dr, dc in directions:
                new_pos = r + dr, c + dc
                if new_pos not in grid:
                    continue
                if grid[new_pos] == grid[(r, c)]:
                    g.add_edge((r, c), new_pos)
    return g

@timer
def solve_part1(input_data):
    grid, rows, cols = get_grid(input_data)
    g = get_graph(grid, rows, cols)
    directions = [(1,0),(0,1),(-1,0),(0,-1)]
    answer = 0
    regions = nx.connected_components(g)
    for region in regions:
        area = len(region)
        perimeter = sum([(r + dr, c + dc) not in region for dr, dc in directions for r, c in region])
        answer += area*perimeter
    return answer

def count_sides(region, grid, nr, nc):
    sides = 0
    # Top sides
    for r in range(nr):
        c = 0
        while c < nc:
            if (r, c) in region and ((r - 1, c) not in grid or (r - 1, c) not in region):
                sides += 1
                while (r, c) in region and ((r - 1, c) not in grid or (r - 1, c) not in region):
                    c += 1
            else:
                c += 1

    # Bottom sides
    for r in range(nr - 1, -1, -1):
        c = 0
        while c < nc:
            if (r, c) in region and ((r + 1, c) not in grid or (r + 1, c) not in region):
                sides += 1
                while (r, c) in region and ((r + 1, c) not in grid or (r + 1, c) not in region):
                    c += 1
            else:
                c += 1

    # Left sides
    for c in range(nc):
        r = 0
        while r < nr:
            if (r, c) in region and ((r, c - 1) not in grid or (r, c - 1) not in region):
                sides += 1
                while (r, c) in region and ((r, c - 1) not in grid or (r, c - 1) not in region):
                    r += 1
            else:
                r += 1

    # Right sides
    for c in range(nc - 1, -1, -1):
        r = 0
        while r < nr:
            if (r, c) in region and ((r, c + 1) not in grid or (r, c + 1) not in region):
                sides += 1
                while (r, c) in region and ((r, c + 1) not in grid or (r, c + 1) not in region):
                    r += 1
            else:
                r += 1
    return sides

@timer
def solve_part2(input_data):
    grid, rows, cols = get_grid(input_data)
    g = get_graph(grid, rows, cols)
    directions = [(1,0),(0,1),(-1,0),(0,-1)]
    answer = 0
    regions = nx.connected_components(g)
    for region in regions:
        area = len(region)
        sides = count_sides(region, grid, rows, cols)
        # print(f"Region with area={area}, sides={sides}, and product={area*sides}")
        answer += area*sides
    return answer

if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))
    input_data = read_input("input.txt", base_path=script_dir)
    print("Solution to Part 1:", solve_part1(input_data))
    print("Solution to Part 2:", solve_part2(input_data))
