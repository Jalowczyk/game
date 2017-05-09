import sys, tty, termios, os, csv

def create_board():
    board_file = open('board.csv', 'r')
    board = []
    for line in board_file:
        line = list(line[:-1])
        board.append(line)

    board_file.close()

    return board


def print_board(board):
    """Prints board."""

    os. system("clear")
    for row in board:
        for sign in row:
            print(sign, end="")
        print('')


def insert_player(board, y, x):
    """Inserts player in board in certain (x, y) position."""
    player = "@"
    board[y][x] = player

    return board
