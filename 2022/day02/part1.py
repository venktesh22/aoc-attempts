from utils.file_io import read_input
from utils.timer import timer  # Importing the timer wrapper
import os

@timer
def solve_part1(input_data):
    player_dict_score = {'A': 1, 'B': 2, 'C': 3, 'X': 1, 'Y':2, 'Z':3}
    code_to_work = {'A': "Rock", 'B': "Paper", "C": "Scissor", 'X': "Rock", 'Y': "Paper", "Z": "Scissor"}
    def does_move1_win(m1,m2):
        return (m1=="Paper" and m2=="Rock") or (m1=="Rock" and m2=="Scissor") or (m1=="Scissor" and m2=="Paper")

    sum_val = 0
    for row in input_data.split('\n'):
        opp_move, your_move = code_to_work[row.split()[0]], code_to_work[row.split()[1]];
        if opp_move == your_move:
            sum_val += player_dict_score[row.split()[1]] + 3
        elif does_move1_win(your_move, opp_move):
            sum_val += player_dict_score[row.split()[1]] + 6
        else:
            sum_val += player_dict_score[row.split()[1]] + 0

        
    
    return sum_val

if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))
    input_data = read_input("input.txt", base_path=script_dir)
    print("Solution to Part 1:", solve_part1(input_data))
