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
    ans = 0
    for i in range(len(input_data)):
        if i< len(input_data)/2:
            if input_data[i]==input_data[i+int(len(input_data)/2)]:
                ans += int(input_data[i])
        else:
            if input_data[i]==input_data[ i + int(len(input_data)/2) - len(input_data)]:
                ans += int(input_data[i])
    # Add your solution logic here
    return ans

if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))
    input_data = read_input("input.txt", base_path=script_dir)
    print("Solution to Part 2:", solve_part2(input_data))
