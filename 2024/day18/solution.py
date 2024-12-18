import re
import numpy as np
from collections import Counter
from itertools import accumulate, product, permutations, combinations
from utils.file_io import read_input
from utils.timer import timer
import os
import networkx as nx

def shortest_path_length_in_grid(grid):
    G = nx.Graph()
    rows, cols = len(grid), len(grid[0])
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '.':
                for dr, dc in [(1,0),(0,1),(-1,0),(0,-1)]:
                    nr, nc = r+dr, c+dc
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] in '.':
                        G.add_edge((r,c),(nr,nc))
    start, goal = (0,0),(rows-1,cols-1)
    if start not in G or goal not in G:
        return None
    try:
        return nx.shortest_path_length(G, start, goal)
    except nx.NetworkXNoPath:
        return None

@timer
def solve_part1(input_data):
    all_coords = input_data.split("\n")
    grid = [["." for _ in range(71)] for _ in range(71)]
    # print(grid)
    for coord in all_coords[:1024]:
        x, y = map(int,re.findall(r'\d+', coord))
        # print(x,y)
        grid[y][x] = "#"
    
    return shortest_path_length_in_grid(grid)

@timer
def solve_part2(input_data):
    all_coords = input_data.split("\n")
    grid = [["." for _ in range(71)] for _ in range(71)]
    # print(grid)
    for coord in all_coords[:2024]:
        x, y = map(int,re.findall(r'\d+', coord))
        # print(x,y)
        grid[y][x] = "#"
    for coord in all_coords[2024:]:
        x, y = map(int,re.findall(r'\d+', coord))
        grid[y][x] = "#"
        path_length = shortest_path_length_in_grid(grid)
        if path_length is None:
            print("No path exists.")
            return coord
        # else:
        #     print(f"Adding coord {coord}, the shortest path length is {path_length}")
            

if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))
    input_data = read_input("input.txt", base_path=script_dir)
    print("Solution to Part 1:", solve_part1(input_data))
    print("Solution to Part 2:", solve_part2(input_data))
