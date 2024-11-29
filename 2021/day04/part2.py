from utils.file_io import read_input
from utils.timer import timer  # Importing the timer wrapper
import os
import copy

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
def solve_part2(input_data):
    """
    Solves Part 2 of the puzzle.

    Args:
        input_data (str): The raw input data as a string.

    Returns:
        Any: The solution to Part 2.
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
    grid_indices = list(range(len(all_grids)))
    for i in range(6, len(sequence_data) + 1):
        # print(grid_indices)
        sublist = sequence_data[:i]
        if len(grid_indices) == 1:
            g = all_grids[grid_indices[0]]
            # print('Sublist=',sublist)
            sum_nums = sum(n for r in g for n in r if n not in sublist)
            sequence_last_term = sequence_data[i-1]
            # print(f"sequence last term = {sequence_last_term}")
            # print(f"Sum numbers = {sum_nums}")
            break
        
        for j in grid_indices[:]: #looping over a copy of it!
            g = all_grids[j]
            if evaluate_bingo_statisfied(g, sublist):
                grid_indices.remove(j)

    # print('i=',i,'sequence_data',len(sequence_data))
    #run though this last grid till bingo is hit
    for k in range(i,len(sequence_data)+1):
        g = all_grids[grid_indices[0]]
        sublist = sequence_data[:k]
        if evaluate_bingo_statisfied(g, sublist):
            sum_nums = sum(n for r in g for n in r if n not in sublist)
            sequence_last_term = sequence_data[k-1]
            print(f"sequence last term = {sequence_last_term}")
            print(f"Sum numbers = {sum_nums}")
            break

    return sum_nums * sequence_last_term
    

if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))
    input_data = read_input("input.txt", base_path=script_dir)
    print("Solution to Part 2:", solve_part2(input_data))
