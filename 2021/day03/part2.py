from utils.file_io import read_input
from utils.timer import timer  # Importing the timer wrapper
import os
import copy
from collections import Counter


def zip_trim(row_string_list, upper=True):
    columnintlist_list = list(zip(*row_string_list)) #first swap columns as rows
    if upper:
        c = Counter(columnintlist_list[0]).most_common(2)
        if c[0][1] == c[1][1]:
            #there is a tie.
            char_common = '1'
        else:
            char_common = c[0][0] #most common
        subset_list = [s[1:] for s in row_string_list if s[0]==char_common] #return all remaining string with first char removed
    else:
        c = Counter(columnintlist_list[0]).most_common(2)
        if c[0][1] == c[1][1]:
            #there is a tie.
            char_common = '0'
        else:
            char_common = c[1][0] #least common
        subset_list = [s[1:] for s in row_string_list if s[0]==char_common] #return all remaining string with first char removed
    
    return char_common, subset_list

@timer
def solve_part2(input_data):
    """
    Solves Part 2 of the puzzle.

    Args:
        input_data (str): The raw input data as a string.

    Returns:
        Any: The solution to Part 2.
    """
    row_string_list = input_data.split('\n')
    row_string_list_duplicate =  copy.deepcopy(row_string_list)
    row_string_list_copy = copy.deepcopy(row_string_list)
    c1 = ""
    c2 = ""
    for i in range(len(row_string_list_copy[0])):
        # print(c1, row_string_list)
        if(len(row_string_list) > 1):
            c, row_string_list = zip_trim(row_string_list)
            c1 += c
        elif(len(row_string_list) == 1):
            c1 += row_string_list[0]
            row_string_list = []
        # print(c2, row_string_list_duplicate)
        if(len(row_string_list_duplicate) > 1):
            c, row_string_list_duplicate = zip_trim(row_string_list_duplicate, False)
            c2 += c
        elif(len(row_string_list_duplicate) == 1):
            c2 += row_string_list_duplicate[0]
            row_string_list_duplicate = []

    o2gen = 0
    for i,c in enumerate(reversed(c1)):
        o2gen += (2**i)*(int(c))
    co2gen = 0
    for i,c in enumerate(reversed(c2)):
        co2gen += (2**i)*(int(c))
    # print('Final oxygen generator is',c1,'with decimal equivalent=',o2gen)
    # print('Final co2 generator is',c2,'with decimal equivalent=',co2gen)
    return o2gen*co2gen

if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))
    input_data = read_input("input.txt", base_path=script_dir)
    print("Solution to Part 2:", solve_part2(input_data))
