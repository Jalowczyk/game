import sys, tty, termios, os, csv
from graphical_user_interface import *
from screens import *
from create_board import *


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

def is_move_possible(y, x, obstacles_letters, board):
    return board[y][x] not in obstacles_letters

def move_by(y, x, y_change, x_change):
    y += y_change
    x += x_change

    return y, x

def control_position(input_key):

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
    else:
        x_diff = 0
        y_diff = 0

    return x_diff, y_diff


def is_key_in_inventory(key, added_items):
    return key in added_items


def is_touching_horse(position_on_board, horse):
    return position_on_board == horse

def is_touching_table(position_on_board, table_elements):
    return position_on_board in table_elements

def is_note_in_inventory(note, added_items):
    return note in added_items

def main():
    """Handle whole game."""
    os.system("clear")
    read_welcome_screen_file()
    x_hero = 1  #starting position of player
    y_hero = 1
    dutifulness = 100
    lives = 3
    board = create_board()

    obstacles_letters = ["X", "_", "|", "♞", "/"]
    table_elements = ["_", "|"]
    door = "/"
    blood = "~"
    inventory = {"purple key": 2, "dope": 3}
    added_items = []
    horse = "♞"

    note = "note"
    key = "key"

    input_key = getch()  #control

    while input_key != "q":
        x_diff = 0
        y_diff = 0

        input_key = getch()
        x_diff, y_diff = control_position(input_key)

        if is_move_possible(y_hero + y_diff, x_hero + x_diff, obstacles_letters, board):
            y_hero, x_hero = move_by(y_hero, x_hero, y_diff, x_diff)


        if is_touching_horse(board[y_hero + y_diff][x_hero + x_diff], horse) and not is_key_in_inventory(key, added_items):
            added_items.append(key)
            add_to_inventory(inventory, added_items)

        if is_touching_table(board[y_hero + y_diff][x_hero + x_diff], table_elements) and not is_note_in_inventory(note, added_items) and is_key_in_inventory(key, added_items):
            added_items.append(note)
            add_to_inventory(inventory, added_items)

        if board[y_hero + y_diff][x_hero + x_diff] == blood:
            dutifulness = subtract_dutifulness(dutifulness)

        if board[y_hero + y_diff][x_hero + x_diff] == door and door in obstacles_letters and key in inventory:
            obstacles_letters.remove(door)



        elif input_key == "q":
            sys.exit()

        board = create_board()
        insert_player(board, y_hero, x_hero)
        print_board(board)
        print_graphical_user_interface(inventory, dutifulness, lives)
        print_description()


main()
