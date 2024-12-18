import re
import numpy as np
from collections import Counter
from itertools import accumulate, product, permutations, combinations
from utils.file_io import read_input
from utils.timer import timer
import os
import networkx as nx

def count_unique_coordinates(shortest_path, coords):
    for node in shortest_path:
        if node == 'START':
            continue
        # node is an edge in the original graph: ((r1,c1),(r2,c2))
        u, v = node
        coords.add(u)
        coords.add(v)
    return coords

@timer
def solve_part1_2(input_data):
    grid = []
    for j, row in enumerate(input_data.split('\n')):
        row_list = [k for k in row]
        if 'S' in row_list:
            start_pos = (j,row_list.index('S'))
        if 'E' in row_list:
            end_pos = (j,row_list.index('E'))
        grid.append(row_list)
    
    G = nx.DiGraph()
    rows, cols = len(grid), len(grid[0])
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] in ['.','S','E']:
                for dr, dc in [(1,0),(0,1),(-1,0),(0,-1)]:
                    nr, nc = r+dr, c+dc
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] in ['.','S','E']:
                        G.add_edge((r,c), (nr,nc))
                        G.add_edge((nr,nc), (r,c))
    
    L = nx.line_graph(G)
    #assign direction to an edge
    for edge in G.edges():
        u, v = edge
        direction = 'H' if u[0]==v[0] else 'V'
        L.nodes[edge]['direction'] = direction
    # set weights in line graph
    for e1, e2 in L.edges():
        d1 = L.nodes[e1]['direction']
        d2 = L.nodes[e2]['direction']
        if d1 == d2:
            L[e1][e2]['weight'] = 1
        else:
            L[e1][e2]['weight'] = 1001
    S = 'START'
    L.add_node(S)
    
    # From the start node, we connect to edges in G that originate at start_pos.
    # If that edge is horizontal, initial cost = 2, else 1002 (since we start facing horizontal).
    # print(start_pos)
    # print(L.nodes)
    for neighbor in G.neighbors(start_pos):
        first_edge = (start_pos, neighbor) if (start_pos, neighbor) in G.edges() else (neighbor, start_pos)
        # print(first_edge)
        first_dir = L.nodes[first_edge]['direction']
        # Cost depends on whether the first edge is horizontal or vertical
        initial_cost = 1 if first_dir == 'H' else 1001
        L.add_edge(S, first_edge, weight=initial_cost)
    
    candidate_end_nodes = []
    for neighbor in G.neighbors(end_pos):
        # Edge in G that touches end_pos
        if (end_pos, neighbor) in G.edges():
            candidate_end_nodes.append((end_pos, neighbor))
        elif (neighbor, end_pos) in G.edges():
            candidate_end_nodes.append((neighbor, end_pos))

    # Now find shortest paths from S to any of these candidate nodes in L
    best_path = None
    best_length = float('inf')
    best_targets = []
    for target in candidate_end_nodes:
        try:
            path_length = nx.shortest_path_length(L, S, target, weight='weight')
            if path_length < best_length:
                best_length = path_length
                best_targets = []
                best_targets.append(target)
                best_path = nx.shortest_path(L, S, target, weight='weight')
            elif path_length == best_length:
                best_targets.append(target)
        except nx.NetworkXNoPath:
            pass
    
    if best_path is not None:
        # print("Shortest path in L to reach end_pos is:", best_path)
        print("Shortest Path length (Part 1):", best_length-1)
    else:
        print("No path found that reaches end_pos.")

    # print("Best targets are", best_targets)
    common_nodes = set()
    for target in best_targets:
        try:
            # print("Evaluating target", target)
            paths = nx.all_shortest_paths(L, S, target, weight='weight')
            for k, path in enumerate(paths):
                common_nodes = count_unique_coordinates(path, common_nodes)
                # print(f'Path {k} has {path_length} weight. Common_nodes thus far = {len(common_nodes)}')

        except nx.NetworkXNoPath:
            pass
    print("Num common nodes are (Part 2)", len(common_nodes))

    return None

if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))
    input_data = read_input("input.txt", base_path=script_dir)
    print("Solution to Parts 1 and 2:", solve_part1_2(input_data))
    # print("Solution to Part 2:", solve_part2(input_data))
