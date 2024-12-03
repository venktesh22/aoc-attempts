from utils.file_io import read_input
from utils.timer import timer  # Importing the timer wrapper
import os

@timer
def solve_part2(input_data):
    input_data = "do()"+input_data #ensure the first few mul() are valid
    import re
    # first, I will find all do() or don't() in the string
    boundary_pattern = re.compile(r"do\(\)|don't\(\)")  
    boundaries = list(boundary_pattern.finditer(input_data)) #finditer will get an iterator and re.Match objects
    # print("Boundary pattern", boundaries)
    # for match in boundaries:
    #     print(f"Found: {match.group()} at {match.start()}-{match.end()}")

    # next, I extract substrings between from do() till next do() or don't()
    results = []
    for i in range(len(boundaries)):
        start = boundaries[i].start()
        end = boundaries[i + 1].start() if i + 1 < len(boundaries) else len(input_data)
        block = input_data[start:end].strip()
        # print("Block is", block)
        #Only include blocks that start with "do()"
        if block.startswith("do()"):
            results.append(block)

    ans = 0
    for valid_block in results:
        ans += sum(int(a) * int(b) for a, b in re.findall(r'mul\((\d+),(\d+)\)', valid_block))

    return ans

if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))
    input_data = read_input("input.txt", base_path=script_dir)
    print("Solution to Part 2:", solve_part2(input_data))
