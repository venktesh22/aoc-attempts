from utils.file_io import read_input
from utils.timer import timer  # Importing the timer wrapper
import os

def sumFun(n):
    return n*(n+1)/2

@timer
def solve_part2(input_data):
    """
    Solves Part 2 of the puzzle.

    Args:
        input_data (str): The raw input data as a string.

    Returns:
        Any: The solution to Part 2.
    """
    #use the property that it is still the median x(x+1)/2
    #but if tied then
    import numpy as np
    from collections import Counter
    nums = [int(s) for s in input_data.split(",")]
    counter_num = Counter(sorted(nums))
    print(counter_num)
    # import matplotlib.pyplot as plt
    # plt.hist(nums, bins='auto', edgecolor='black')
    # plt.xlabel('Value')
    # plt.ylabel('Frequency')
    # plt.title('Histogram of Numbers')
    # plt.show()

    print(len(nums))
    return min( sum(sumFun(abs(n-np.ceil(np.mean(nums)))) for n in nums), sum(sumFun(abs(n-np.floor(np.mean(nums)))) for n in nums))

if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))
    input_data = read_input("input.txt", base_path=script_dir)
    print("Solution to Part 2:", solve_part2(input_data))
