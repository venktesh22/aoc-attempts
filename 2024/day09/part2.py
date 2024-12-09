from utils.file_io import read_input
from utils.timer import timer  # Importing the timer wrapper
import os
from copy import deepcopy

def convert_to_simple_list(data):
    # Determine the final length needed
    # The maximum 'end' value will determine the size of the list.
    max_end = max(entry[2] for entry in data)
    result = [None] * max_end

    for entry in data:
        _id, start, end, diff = entry
        # Fill the result list from start to end-1
        for i in range(start, end):
            result[i] = _id
    
    return result

@timer
def solve_part2(input_data):
    # input_data = '''2333133121414131402'''
    # input_data = '''12345'''
    import re
    all_nums = list(map(int,re.findall(r'\d',input_data)))
    # print(all_nums)
    #first let compute start and end of each id
    start_index = 0
    all_num_start_end_index = []
    
    j=-1
    for i in range(0,len(all_nums),2):
        end_index = start_index + all_nums[i] #doesn't include
        all_num_start_end_index.append([int(i/2),start_index,end_index, end_index-start_index])
        if i+1 >= len(all_nums):
            break
        all_num_start_end_index.append([j, end_index, end_index + all_nums[i+1],all_nums[i+1]])
        j-=1
        start_index = end_index + all_nums[i+1]
    # print(all_num_start_end_index)
    copy_tup_list = deepcopy(all_num_start_end_index)
    print(convert_to_simple_list(copy_tup_list),'\n')
    #for sample input above prints
    #[0, 0, -1, -1, -1, 1, 1, 1, -2, -2, -2, 2, -3, -3, -3, 3, 3, 3, -4, 4, 4, -5, 5, 5, 5, 5, -6, 6, 6, 6, 6, -7, 7, 7, 7, -8, 8, 8, 8, 8, 9, 9]
    first_start_pos = len(copy_tup_list)-1
    first_start_neg = 0

    while True:
        all_num_start_end_index = copy_tup_list
        # print(convert_to_simple_list(all_num_start_end_index),'\n')
        found_new = False
        for i, tup in reversed(list(enumerate(all_num_start_end_index))):
            if tup[0]>0 and tup[0]< first_start_pos:
                first_start_pos = tup[0]
                found_new = True
                break

        if not found_new:
            break
        id,start,end,length = tup
        # print("Evaluating", tup)
        for j, tup2 in enumerate(all_num_start_end_index):
            id2,start2,end2,length2 = tup2
            if j >= first_start_neg and id2<0:
                if tup2[3]>=length and i>=j:
                    # print("Valid space found", tup2)
                    if tup2[3]-length == 0:
                        #we don't create additional tuple and simply replace the old one
                        copy_tup_list[j][0] = id
                        copy_tup_list[i][0] = id2
                    else:
                        #we now replace the old sublist with two sublists
                        copy_tup_list.insert(j,[id,start2,end2,length])
                        copy_tup_list[j+1][1] += length
                        copy_tup_list[j+1][3] = length2-length
                        # first_start_neg = j+1
                        copy_tup_list[i+1][0] = id2
                    
                    break
                # else:
                    # print("Invalid")
    result = convert_to_simple_list(all_num_start_end_index)
    print(result)

    cum_sum = 0
    for i, val in enumerate(result):
        if val > 0:
            cum_sum += i*val
    print(cum_sum)
    # print(mega_list)
    

    return cum_sum

if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))
    input_data = read_input("input.txt", base_path=script_dir)
    print("Solution to Part 2:", solve_part2(input_data))
