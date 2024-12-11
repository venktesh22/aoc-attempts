from utils.file_io import read_input
from utils.timer import timer  # Importing the timer wrapper
import os

@timer
def solve_part2(input_data):
    player_dict_score = {'A': 1, 'B': 2, 'C': 3, 'X': 1, 'Y':2, 'Z':3}
    code_to_work = {'A': "Rock", 'B': "Paper", "C": "Scissor"}
    move_to_letter = {"Rock": 'A', "Paper": 'B', "Scissor": 'C'}
    outcome = {'X': "Lose", 'Y': "Draw", "Z": "Win"}
    
    def does_move1_win(m1,m2):
        return (m1=="Paper" and m2=="Rock") or (m1=="Rock" and m2=="Scissor") or (m1=="Scissor" and m2=="Paper")

    sum_val = 0
    for row in input_data.split('\n'):
        opp_move, out = code_to_work[row.split()[0]], outcome[row.split()[1]];
        if out == "Draw":
            sum_val += player_dict_score[row.split()[0]] + 3
        else:
            for my_move in ["Rock", "Paper", "Scissor"]:
                if my_move!=opp_move:
                    if out=="Win" and does_move1_win(my_move, opp_move):
                        sum_val += player_dict_score[move_to_letter[my_move]] + 6
                    elif out=="Lose" and not does_move1_win(my_move, opp_move):
                        sum_val += player_dict_score[move_to_letter[my_move]] + 0

    return sum_val

if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))
    input_data = read_input("input.txt", base_path=script_dir)
    print("Solution to Part 2:", solve_part2(input_data))
