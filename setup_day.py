import os
import datetime

def setup_day(day=None, year=None):
    """
    Creates the folder and files for the specified day and year, including solution.py,
    input.txt, and test_dayXX.py. Defaults to today's day and year if not specified.
    """
    # Determine the year
    if year is None:
        year = datetime.datetime.now().year
    elif isinstance(year, str):
        try:
            year = int(year)
        except ValueError:
            raise ValueError("Year must be an integer or a string that can be converted to an integer.")

    # Determine the day
    if day is None:
        day = datetime.datetime.now().day
    elif isinstance(day, str):
        try:
            day = int(day)
        except ValueError:
            raise ValueError("Day must be an integer or a string that can be converted to an integer.")

    # Validate inputs
    if not (1 <= day <= 25):
        raise ValueError("Day must be between 1 and 25.")
    if not (2015 <= year <= datetime.datetime.now().year):
        raise ValueError(f"Year must be between 2015 and {datetime.datetime.now().year} (inclusive).")

    # Create the folder structure
    day_folder = f"{year}/day{day:02d}"
    os.makedirs(day_folder, exist_ok=True)

    # Create empty __init__.py files in relevant folders
    for folder in [str(year), day_folder]:
        init_path = os.path.join(folder, "__init__.py")
        if not os.path.exists(init_path):
            with open(init_path, "w") as f:
                f.write("")  # Create an empty __init__.py file

    # File paths
    input_file = os.path.join(day_folder, "input.txt")
    solution_file = os.path.join(day_folder, "solution.py")
    test_file = os.path.join(day_folder, f"test_day{day:02d}.py")

    # Create input.txt
    if not os.path.exists(input_file):
        with open(input_file, "w") as f:
            f.write("")  # Empty file for input

    # Create solution.py
    if not os.path.exists(solution_file):
        with open(solution_file, "w") as f:
            f.write(f"""import re
import numpy as np
from collections import Counter
from itertools import accumulate, product, permutations, combinations
from utils.file_io import read_input
from utils.timer import timer
import os

@timer
def solve_part1(input_data):
    \"\"\"
    Solves Part 1 of the puzzle.

    Args:
        input_data (str): The raw input data as a string.

    Returns:
        Any: The solution to Part 1.
    \"\"\"
    # Add your solution logic here
    return None

@timer
def solve_part2(input_data):
    \"\"\"
    Solves Part 2 of the puzzle.

    Args:
        input_data (str): The raw input data as a string.

    Returns:
        Any: The solution to Part 2.
    \"\"\"
    # Add your solution logic here
    return None

if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))
    input_data = read_input("input.txt", base_path=script_dir)
    print("Solution to Part 1:", solve_part1(input_data))
    print("Solution to Part 2:", solve_part2(input_data))
""")

    # Create test_dayXX.py
    if not os.path.exists(test_file):
        with open(test_file, "w") as f:
            f.write(f"""import pytest
from day{day:02d}.solution import solve_part1, solve_part2
import os

def test_solve_part1():
    input_data = \"\"\"1
2
3
4\"\"\"  # Example input
    expected_output = None  # Replace with the expected output
    assert solve_part1(input_data) == expected_output

def test_solve_part2():
    input_data = \"\"\"1
2
3
4\"\"\"  # Example input
    expected_output = None  # Replace with the expected output
    assert solve_part2(input_data) == expected_output
""")

    print(f"Setup complete for Year {year}, Day {day:02d}")


if __name__ == "__main__":
    import sys

    # Parse command-line arguments
    args = sys.argv[1:]
    day = None
    year = None

    if len(args) >= 1:
        day = args[0]
    if len(args) == 2:
        year = args[1]

    setup_day(day, year)