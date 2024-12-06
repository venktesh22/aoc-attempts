from utils.file_io import read_input
from utils.timer import timer  # Importing the timer wrapper
import os

def pretty_print_grids(grid1, grid2):
    for row1, row2 in zip(grid1, grid2):
        print(' '.join(row1) + "   |   " + ' '.join(row2))
    print('\n')

@timer
def solve_part2(input_data):

    grid = [list(row) for row in input_data.split('\n')]
    rows, cols = len(grid), len(grid[0])
    for y, row in enumerate(grid):
        if '^' in row:
            start_y, start_x = y, row.index('^')
    x ,y, direction = start_x, start_y, '^'

    def is_valid(x, y):
        return 0 <= x < cols and 0 <= y < rows
    
    move = {
        "^": (0,-1),  
        ">": (1,0),   
        "v": (0,1),   
        "<": (-1,0)    
    }

    ninety_degree = {"^":">", ">":"v", "v":"<", "<":"^"}

    valid_pos = 0
    print_options = False
    for y0 in range(rows):
        for x0 in range(cols):

            grid = [list(row) for row in input_data.split('\n')] #reset grid
            if grid[y0][x0]== '#' or grid[y0][x0]== '^':
                continue
            dir_grid = [['.' for _ in range(len(grid[0]))] for _ in range(len(grid))]
            grid[y0][x0]= 'O'

            #now ensure that every run of loop below either direction changes or we mark a new X
            x ,y, direction = start_x, start_y, '^'
            cycle_found = False
            while is_valid(x,y):
                if print_options:
                    pretty_print_grids(grid, dir_grid)
                dx,dy = move[direction]
                if not is_valid(x+dx,y+dy):
                    grid[y][x] = 'X'
                    break
                if grid[y+dy][x+dx] == '#' or grid[y+dy][x+dx] == 'O':
                    direction = ninety_degree[direction]
                    # dir_grid[y][x] += direction
                else:
                    if grid[y][x] == 'X' and direction in dir_grid[y][x]:
                        #already visited this cell in same direction
                        cycle_found = True
                        break
                    grid[y][x] = 'X'
                    dir_grid[y][x] += direction
                    x ,y = x+dx, y+dy
            
            if cycle_found:
                if printOptions:
                    print(f"Cycle found at {y0},{x0}!")
                valid_pos += 1
            # printOptions = False
    
    return valid_pos

if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))
    input_data = read_input("input.txt", base_path=script_dir)
    print("Solution to Part 2:", solve_part2(input_data))
