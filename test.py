import csv

def create_board():
    board_file = open('board.csv', 'r')
    board = []
    for line in board_file:
        line = list(line[:-1])
        board.append(line)

    board_file.close()

    return board

def open_door(board):

    board[1][3] = " "


    print(board)

    with open("board.csv", "w", newline="") as board_file:
        writer = csv.writer(board_file)
        writer.writerow(board)

    board_file.close()

board = create_board()
open_door(board)
