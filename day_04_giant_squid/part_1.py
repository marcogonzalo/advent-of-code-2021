import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.input_reader import *

def calc_final_score(bingo_input):
    numbers_played = bingo_input[0].split(',')
    boards = get_boards(bingo_input[2:])
    unplayed_sum = 0
    board_num = None
    for num in numbers_played:
        board_num = check_boards(boards, num)
        if board_num is not None:
            break

    for r in range(5):
        for c in range(5):
            if boards[board_num][r][c] != '*':
                unplayed_sum += int(boards[board_num][r][c])    

    return unplayed_sum * int(num)

def check_boards(boards, number):
    for b in range(len(boards)):
        for i in range(5):
            horizontal_counter = 0
            vertical_counter = 0

            for j in range(5):
                if boards[b][i][j] == number:
                    boards[b][i][j] = '*'
                
                if boards[b][j][i] == '*':
                    vertical_counter += 1

                if boards[b][i][j] == '*':
                    horizontal_counter += 1

            if horizontal_counter == 5 or vertical_counter == 5:
                return b
    return None

def get_boards(boards_input):
    board_list = []
    board = []
    for line in boards_input:
        if len(line) == 0 and len(board) > 0:
            board_list.append(list(board))
            board = []
        else:
            board.append(line.split())
    board_list.append(list(board))
    return board_list

def main():
    file_path = os.path.dirname(__file__)  + '/input.txt'
    values = get_input_array(filename=file_path)
    life_support_rating = calc_final_score(values)
    print("Final score in winner board: {}".format(life_support_rating))


main()
