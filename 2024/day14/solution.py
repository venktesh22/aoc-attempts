import re
import numpy as np
from collections import Counter
from itertools import accumulate, product, permutations, combinations
from utils.file_io import read_input
from utils.timer import timer
import os

from PIL import Image, ImageDraw, ImageFont


def grid_to_image(grid, filename="test_.png"):
    lines = ["".join("*" if k > 0 else " " for k in row) for row in grid]
    font = ImageFont.load_default()
    temp_img = Image.new("RGB", (1,1))
    temp_draw = ImageDraw.Draw(temp_img)
    w = max(temp_draw.textbbox((0,0), line, font=font)[2] for line in lines)
    line_height = temp_draw.textbbox((0,0), "A", font=font)[3]
    h = line_height * len(lines)
    img = Image.new("RGB", (w, h), "white")
    draw = ImageDraw.Draw(img)
    y = 0
    for line in lines:
        draw.text((0, y), line, font=font, fill="black")
        y += line_height
    img.save(filename)

def pretty_print_grids(grid1):
    for row1 in grid1:
        print("".join("*" if k > 0 else "" for k in row1))
    print('\n')

@timer
def solve_part1(input_data):
    max_tall, max_wide = 103, 101 #103, 101
    grid = [[0 for _ in range(max_wide)] for _ in range(max_tall)]
    def valid_update(cx, cy, vx, vy):
        nx = (cx + vx) % max_wide
        ny = (cy + vy) % max_tall
        return nx, ny

    robots = []
    for row in input_data.split('\n'):
        px,py,vx,vy = map(int, re.findall(r'-?\d+',row))
        robots.append([px,py,vx,vy])
        grid[py][px] += 1
    pretty_print_grids(grid)
    for step in range(100):
        for robot in robots:
            cx,cy,vx,vy = robot
            nx,ny = valid_update(cx,cy,vx,vy)
            grid[cy][cx] -= 1
            grid[ny][nx] += 1
            robot[0] = nx
            robot[1] = ny
    # pretty_print_grids(grid)
    # grid_to_image(grid,f"2024/day14/test_{step+1}.png")
    #get quadrant data
    fQ, sQ, tQ, foQ = 0 ,0 ,0, 0
    for j , row in enumerate(grid):
        for i, col  in enumerate(row):
            if col > 0:
                if i < int(max_wide/2) and j < int(max_tall/2):
                    fQ += col
                elif i > int(max_wide/2) and j < int(max_tall/2):
                    sQ += col
                elif i < int(max_wide/2) and j > int(max_tall/2):
                    tQ += col
                elif i > int(max_wide/2) and j > int(max_tall/2):
                    foQ += col
    print(fQ, sQ, tQ, foQ)
    return fQ*sQ*tQ*foQ

@timer
def solve_part2(input_data):
    # Visual observations reveal that columns line up from 79th itr then in 
    # increments of 101
    # Similarly, rows line up from 52th itr then in increments of 103.
    # So I find the least common multiple of 101 and 103 considering the offset.
    col_repeat = [i for i in range(79, 17000, 101)]
    row_repeat = [j for j in range(52,17000,103)]
    for i in row_repeat:
        if i in col_repeat:
            # print(i)
            break
    return i

if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))
    input_data = read_input("input.txt", base_path=script_dir)
    print("Solution to Part 1:", solve_part1(input_data))
    print("Solution to Part 2:", solve_part2(input_data))
