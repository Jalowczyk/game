import sys, tty, termios, os, csv

HEADER = '\033[95m'
OKBLUE = '\033[94m'
OKGREEN = '\033[92m'
WARNING = '\033[93m'
FAIL = '\033[91m'
ENDC = '\033[0m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'

sign_colours = {"X": OKBLUE}

def create_board():
    board_file = open('board.csv', 'r')
    board = []
    for line in board_file:
        line = list(line[:-1])
        board.append(line)

    board_file.close()

    return board

def get_coloured_sign(sign):
    if sign in sign_colours:
        return sign_colours[sign] + sign + ENDC
    else:
        return sign

def print_board(board):
    """Prints board."""

    os. system("clear")
    for row in board:
        for sign in row:
            print(get_coloured_sign(sign), end="")
        print('')


def insert_player(board, y, x):
    """Inserts player in board in certain (x, y) position."""
    player = "@"
    board[y][x] = player

    return board
