import sys, tty, termios, os, csv
from graphical_user_interface import print_graphical_user_interface, add_to_inventory, subtract_dutifulness, print_description
from screens import read_welcome_screen_file, read_note1
from create_board import create_board, print_board, insert_player


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

def can_player_move(y, x, obstacles_letters, board):
    return board[y][x] not in obstacles_letters

def move_by(y, x, y_change, x_change):
    y += y_change
    x += x_change

    return y, x


def main():
    """Handle whole game."""
    os.system("clear")
    read_welcome_screen_file()
    x_hero = 1  #starting position of player
    y_hero = 1
    dutifulness = 100
    lives = 3
    board = create_board()
    input_key = getch()

    obstacles_letters = ["X", "_", "|", "♞", "/"]
    table_elements = ["_", "|"]
    door = "/"
    blood = "~"
    inventory = {"purple key": 2, "dope": 3}
    added_items = []
    key_giver = "♞"

    note = "note"
    key = "key"

    while input_key != "q":
        x_diff = 0
        y_diff = 0

        input_key = getch()  #control
        if input_key == "d":
            x_diff = 1
            y_diff = 0
        elif input_key == "a":
            x_diff = -1
            y_diff = 0
        elif input_key == "s":
            x_diff = 0
            y_diff = 1
        elif input_key == "w":
            x_diff = 0
            y_diff = -1

        y_hero_new = y_hero + y_diff
        x_hero_new = x_hero + x_diff
        if can_player_move(y_hero_new, x_hero_new, obstacles_letters, board):
            y_hero, x_hero = move_by(y_hero, x_hero, y_diff, x_diff)
        elif board[y_hero_new][x_hero_new] == key_giver and key not in added_items:
            added_items.append(key)
            add_to_inventory(inventory, added_items)
        elif board[y_hero_new][x_hero_new] in table_elements and note not in added_items and key in inventory:
            added_items.append(note)
            add_to_inventory(inventory, added_items)

        if board[y_hero_new][x_hero_new] == blood:
            dutifulness = subtract_dutifulness(dutifulness)

        if board[y_hero_new][x_hero_new] == door and door in obstacles_letters and key in inventory:
            obstacles_letters.remove(door)



        elif input_key == "q":
            sys.exit()

        board = create_board()
        insert_player(board, y_hero, x_hero)
        print_board(board)
        print_graphical_user_interface(inventory, dutifulness, lives)
        print_description()


main()
