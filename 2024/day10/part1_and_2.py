from utils.file_io import read_input
from utils.timer import timer  # Importing the timer wrapper
import os

def get_valid_neighbors(r, c, grid):
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0
    current_val = grid[r][c]

    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    valid_neighbors_outgoing = []
    valid_neighbors_incoming = []

    for dr, dc in directions:
        nr, nc = r + dr, c + dc
        if 0 <= nr < rows and 0 <= nc < cols:
            if grid[nr][nc] == current_val + 1:
                valid_neighbors_outgoing.append((nr, nc))
            if grid[nr][nc] == current_val - 1:
                valid_neighbors_incoming.append((nr, nc))

    return (valid_neighbors_outgoing, valid_neighbors_incoming)

def get_all_grid_coords_with_val(grid, val):
    coordinates = []
    for i, row in enumerate(grid):
        for j, col in enumerate(row):
            if col==val:
                coordinates.append((i,j))
    return coordinates

@timer
def solve_part1_part2(input_data):
    grid = [[int(a) for a in row] for row in input_data.split('\n')]
    start_points = get_all_grid_coords_with_val(grid, 0)
    end_points = get_all_grid_coords_with_val(grid, 9)
    answer_part1 = 0
    answer_part2 = 0
    for (si, sj) in start_points:
        # Initialize ways_to_reach for each trail head separately
        ways_to_reach = [[0 for _ in row] for row in grid]
        ways_to_reach[si][sj] = 1
        #network is topologically sorted, so I can add the # of ways from previous nodes
        for i in range(1,10):
            for ci, cj in get_all_grid_coords_with_val(grid,i):
                _, incoming = get_valid_neighbors(ci,cj,grid)
                for ni,nj in incoming:
                    ways_to_reach[ci][cj] += ways_to_reach[ni][nj]
            # print(ways_to_reach)
        score = sum(1 for (ci, cj) in end_points if ways_to_reach[ci][cj] > 0)
        answer_part1 += score
        rating = sum(ways_to_reach[ci][cj] for (ci, cj) in end_points if ways_to_reach[ci][cj] > 0)
        answer_part2 += rating
        # print(f'Starting from a 0 at ({si},{sj}), I can reach {score} nines using {rating} paths. Thus, score={score},rating={rating}')

    return answer_part1, answer_part2

if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))
    input_data = read_input("input.txt", base_path=script_dir)
    print("Solutions to Part 1 and Part 2 is:", solve_part1_part2(input_data))
