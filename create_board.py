import sys, tty, termios, os, csv

red = '\x1b[0;31;40m'
green = '\x1b[0;32;40m'
yellow = '\x1b[0;33;40m'
blue = '\x1b[0;34;40m'
grey = '\x1b[0;35;40m'
lightgreen = '\x1b[0;36;40m'
white = '\x1b[0;37;40m'
ends = '\x1b[0m'

sign_colours = {"X": OKBLUE, "/": HEADER}

sing_colours = {'♫': red, '♞': red, '☎': blue, 'ᚙ': grey, 'ↈ': , '⍍': , '▆': grey, '⛏': red '⛚': red,
                '✿': yelow, '❽': white, '♨': white,'⚿': red, '✀': blue, '□': , '⟧': white, '▓': white, '☘': green,
                '⏰': yellow, '⛔': red, '⛿': lightgreen, 'Ր': green, 'இ': white, 'ߛ': white,}


('\x1b[6;30;42m' + 'Success!' + '\x1b[0m')
'''
>>>>>>> Stashed changes

def create_board(filename):
    board_file = open(filename, 'r')
    board = []
    for line in board_file:
        line = list(line[:-1])
        board.append(line)

    board_file.close()

    return board
'''
def get_coloured_sign(sign):
    if sign in sign_colours:
        return sign_colours[sign] + sign + ends
    else:
        return sign


print(get_coloured_sign('♞'))
'''
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
'''
