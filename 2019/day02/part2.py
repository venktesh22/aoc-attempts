from utils.file_io import read_input
from utils.timer import timer  # Importing the timer wrapper
import os

@timer
def solve_part2(input_data):
    """
    Solves Part 2 of the puzzle.

    Args:
        input_data (str): The raw input data as a string.

    Returns:
        Any: The solution to Part 2.
    """
    # Add your solution logic here
    

    for v1 in range(100):
        for v2 in range(100):
            num_list = [int(s.strip()) for s in input_data.split(',')]
            num_list[1] = v1
            num_list[2] = v2

            cur_num = num_list[0]
            i = 0;

            while cur_num != 99:
                if cur_num == 1:
                    num_list[num_list[i+3]] = num_list[num_list[i+1]] + num_list[num_list[i+2]]
                    i += 4
                elif cur_num == 2:
                    num_list[num_list[i+3]] = num_list[num_list[i+1]] * num_list[num_list[i+2]]
                    i += 4
                else:
                    break;
                cur_num = num_list[i]
            
            if num_list[0]==19690720:
                print(f"noun={v1} and verb={v2}, and reported value = {100*v1+v2}")
    return None

if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))
    input_data = read_input("input.txt", base_path=script_dir)
    print("Solution to Part 2:", solve_part2(input_data))
