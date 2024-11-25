from utils.file_io import read_input
from utils.timer import timer  # Importing the timer wrapper
import os

def update_x_y_old(x,y,facing,dir,step):
    if facing == 'N':
        x += (step if dir=='R' else -step)
        facing = 'E' if dir=='R' else 'W'
    elif facing == 'S':
        x += (-step if dir=='R' else step)
        facing = 'W' if dir=='R' else 'E'
    elif facing == 'E':
        y += (-step if dir=='R' else step)
        facing = 'S' if dir=='R' else 'N'
    else:
        y += (step if dir=='R' else -step)
        facing = 'N' if dir=='R' else 'S'
    return x,y,facing

# @timer
def update_x_y(x, y, facing, dir, step):
    directions = {
        'N': (1, 0, 'E', 'W'),
        'S': (-1, 0, 'W', 'E'),
        'E': (0, -1, 'S', 'N'),
        'W': (0, 1, 'N', 'S')
    }
    dx, dy, right, left = directions[facing]
    if dir == 'R':
        x, y, facing = x + dx * step, y + dy * step, right
    else:
        x, y, facing = x - dx * step, y - dy * step, left
    return x, y, facing

@timer
def solve_part1(input_data):
    """
    Solves Part 1 of the puzzle.

    Args:
        input_data (str): The raw input data as a string.

    Returns:
        Any: The solution to Part 1.
    """
    # Add your solution logic here
    x ,y , facing = 0,0,'N'
    for string in [s.strip() for s in input_data.split(',')]:
        # print(x,y,facing)
        dir, step = string[0], int(string[1:])
        # print(f"Step {step} in {dir} direction")
        x,y,facing = update_x_y(x,y,facing,dir,step)

    return abs(x)+abs(y)

if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))
    input_data = read_input("input.txt", base_path=script_dir)
    print("Solution to Part 1:", solve_part1(input_data))
