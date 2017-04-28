import sys, tty, termios, os, csv

def read_welcome_screen_file():
    welcome_screen_file = open('welcome_screen.csv', 'r')
    reader_welcome_screen = csv.reader(welcome_screen_file, delimiter = "#")
    welcome_screen = list(reader_welcome_screen)
    welcome_screen_file.close()

    for line in welcome_screen:
        print(*line)

def create_board():
    board_file = open('board.csv', 'r')
    reader_board = csv.reader(board_file)
    board = list(list(reader_board))
    board_file.close()



    return board


def print_board(board):
    """Prints board."""

    os. system("clear")
    for row in board:
        print(*row)


def getch():
    """Connects keys with funcion."""

    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch


def insert_player(board, y, x):
    """Inserts player in board in certain (x, y) position."""
    player = "@"
    board[y][x] = player

    return board


def main():
    """Handle whole game."""

    read_welcome_screen_file()
    x_hero = 1 #starting position of player
    y_hero = 1
    board = create_board()
    print(board)
    x = getch()

    while x != "q":

        x = getch()
        if x == "d":
            if board[y_hero][x_hero + 1] != "X":
                x_hero += 1
        elif x == "a":
            if board[y_hero][x_hero - 1] != "X":
                x_hero -= 1
        elif x == "s":
            if board[y_hero + 1][x_hero] != "X":
                y_hero += 1
        elif x == "w":
            if board[y_hero - 1][x_hero] != "X":
                y_hero -= 1
        elif x == "n":
            board = create_board()
            insert_player(board, y_hero, x_hero)
            print_board(board)
        elif x == "q":
            sys.exit()

        board = create_board()
        insert_player(board, y_hero, x_hero)
        print_board(board)




main()
