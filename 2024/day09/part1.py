from utils.file_io import read_input
from utils.timer import timer  # Importing the timer wrapper
import os
from copy import deepcopy

@timer
def solve_part1(input_data):
    # input_data = '''2333133121414131402'''
    # input_data = '''12345'''
    import re
    all_nums = list(map(int,re.findall(r'\d',input_data)))
    # print(all_nums)
    #first let compute start and end of each id
    start_index = 0
    all_num_start_end_index = {}
    
    for i in range(0,len(all_nums),2):
        end_index = start_index + all_nums[i] #doesn't include
        all_num_start_end_index[int(i/2)] = (int(i/2),start_index,end_index)
        if i+1 >= len(all_nums):
            break
        start_index = end_index + all_nums[i+1]
    # print(all_num_start_end_index)
    mega_list = [-1 for i in range(end_index)]
    for key, value in all_num_start_end_index.items():
        id, start, end = value
        for i in range(start,end):
            mega_list[i]= id
    mega_list_copy = deepcopy(mega_list)
    back_index = len(mega_list)-1
    print('Before list',mega_list)
    for i, val in enumerate(mega_list):
        if val==-1 and i<=back_index:
            # print("Backindex",back_index)
            for j in range(back_index, 0, -1):
                if mega_list_copy[j]!=-1 and j>=i:
                    back_index = j
                    break
            if mega_list_copy[back_index]!=-1:
                mega_list_copy[i] = mega_list_copy[back_index]
                mega_list_copy[back_index] = -1
                # print('Swapping, new list is=',mega_list_copy, 'with back index=', back_index,'forward index=',i)
    print('After list',mega_list_copy)
    cum_sum = 0
    for i, val in enumerate(mega_list_copy):
        if val > 0:
            cum_sum += i*val
    print(cum_sum)

    return cum_sum

if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))
    input_data = read_input("input.txt", base_path=script_dir)
    print("Solution to Part 1:", solve_part1(input_data))
