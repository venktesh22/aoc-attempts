from utils.file_io import read_input
from utils.timer import timer  # Importing the timer wrapper
import os

def evaluate_bingo_statisfied(grid, sequence_revealed):
    """
    Function creates a grid of 0 or 1 if number is already revealed
    Then it checks if any of the row or column sum is 5 or not.
    Could be generalized to nxn grid, but perhaps for future.
    Grid is a list of row list of #s and sequence_revealed is a list.
    """
    grid_boolean = []
    for row in grid:
        grid_boolean.append([1 if num in sequence_revealed else 0 for num in row])
    for row in grid_boolean:
        if (sum(row)==5):
            return True
    for col in zip(*grid_boolean):
        if (sum(col)==5):
            return True
    return False

@timer
def solve_part1(input_data):
    """
    Solves Part 1 of the puzzle.

    Args:
        input_data (str): The raw input data as a string.

    Returns:
        Any: The solution to Part 1.
    """
    #read the input well
    split_data = input_data.split("\n\n")
    sequence_data = [int(s.strip()) for s in split_data[0].split(',')]
    all_grids = []
    for i in range(1,len(split_data)):
        grid_i_string_rows = split_data[i].split("\n")
        grid_i = []
        for row in grid_i_string_rows:
            grid_i.append([int(s.strip()) for s in row.split()])
        all_grids.append(grid_i)
    
    #now process the bingo number reveal process
    sequence_last_term = 0
    sum_nums = 0
    for i in range(6, len(sequence_data) + 1):
        sublist = sequence_data[:i]
        bingo = False
        for g in all_grids:
            if evaluate_bingo_statisfied(g, sublist):
                bingo = True
                sum_nums += sum(n for r in g for n in r if n not in sublist)
                sequence_last_term = sequence_data[i-1]
                # print(f"sequence last term = {sequence_last_term}")
                # print(f"Sum numbers = {sum_nums}")
                break
        if bingo:
            break
    return sum_nums*sequence_last_term

if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))
    input_data = read_input("input.txt", base_path=script_dir)
    print("Solution to Part 1:", solve_part1(input_data))
