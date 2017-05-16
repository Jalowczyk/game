import sys, tty, termios, os, csv
from graphical_user_interface import *
from screens import *
from create_board import *
from interactions import *
from levels import *


def getch():
    """Connects keys with function."""

    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch

def is_move_possible(y, x, obstacles, board):
    return board[y][x] not in obstacles

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

def first_level():
    """Handle game's first level game."""
    os.system("clear")
    read_welcome_screen_file()
    x_hero = 1  #starting position of player
    y_hero = 1
    dutifulness = 100
    lives = 3
    board = create_board('board.csv')
    previous_sign = board[y_hero][x_hero]

    obstacles = ["X", "_", "|", "♞", "/"]
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
        board[y_hero][x_hero] = previous_sign

        if is_move_possible(y_hero + y_diff, x_hero + x_diff, obstacles, board):
            y_hero, x_hero = move_by(y_hero, x_hero, y_diff, x_diff)

        if is_touching_horse(board[y_hero + y_diff][x_hero + x_diff], horse) and not is_key_in_inventory(key, added_items):
            added_items.append(key)
            add_to_inventory(inventory, added_items)

        if is_touching_table(board[y_hero + y_diff][x_hero + x_diff], table_elements) and not is_note_in_inventory(note, added_items) and is_key_in_inventory(key, added_items):
            added_items.append(note)
            add_to_inventory(inventory, added_items)

        if is_touching_blood(board[y_hero + y_diff][x_hero + x_diff], blood):
            dutifulness = subtract_dutifulness(dutifulness)

        if is_touching_door(board[y_hero + y_diff][x_hero + x_diff], door) and is_door_closed(obstacles, door) and is_key_in_inventory(key, added_items):
            obstacles.remove(door)
            return dutifulness, lives, inventory

        elif input_key == "q":
            sys.exit()

        previous_sign = board[y_hero][x_hero]
        insert_player(board, y_hero, x_hero)
        print_board(board)
        print_graphical_user_interface(inventory, dutifulness, lives)
        print_first_level_description()

def second_level(dutifulness, lives, inventory):
    """Handle game's second level game."""
    os.system("clear")
    x_hero = 1  #starting position of player
    y_hero = 1
    board = create_board("las.csv")
    previous_sign = board[y_hero][x_hero]

    obstacles = ["▓", "☘", "༊", "✀", "⛏"]
    added_items = []
    blood = "~"
    twanas_list = ["௸", "௺", "இ", "௫", "௵", "ඖ", "ඣ", "ඐ", "ණ"]
    twanas = "twanas"

    input_key = getch()  #control

    while input_key != "q":
        x_diff = 0
        y_diff = 0

        input_key = getch()
        x_diff, y_diff = control_position(input_key)
        board[y_hero][x_hero] = previous_sign

        if is_move_possible(y_hero + y_diff, x_hero + x_diff, obstacles, board):
            y_hero, x_hero = move_by(y_hero, x_hero, y_diff, x_diff)

        if is_touching_blood(board[y_hero + y_diff][x_hero + x_diff], blood):
            dutifulness = subtract_dutifulness(dutifulness)

        if is_touching_twanas(board[y_hero + y_diff][x_hero + x_diff], twanas_list):
            twanas_list.remove(board[y_hero + y_diff][x_hero + x_diff])
            board[y_hero + y_diff][x_hero + x_diff] = " "
            added_items.append(twanas)
            add_to_inventory(inventory, added_items)

        previous_sign = board[y_hero][x_hero]
        insert_player(board, y_hero, x_hero)
        print_board(board)
        print_graphical_user_interface(inventory, dutifulness, lives)
        print_second_level_description()

def main():
    dutifulness, lives, inventory = first_level()
    second_level(dutifulness, lives, inventory)

main()
