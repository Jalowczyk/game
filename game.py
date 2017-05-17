import sys, tty, termios, os, csv
<<<<<<< Updated upstream
from graphical_user_interface import *
from screens import *
from create_board import *
from interactions import *
from levels import *
=======
from graphical_user_interface import print_graphical_user_interface, add_to_inventory, subtract_dutifulness, print_description
from screens import read_welcome_screen_file, read_note1
from create_board import create_board, print_board, insert_player

>>>>>>> Stashed changes


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

<<<<<<< Updated upstream
def is_move_possible(y, x, obstacles, board):
    return board[y][x] not in obstacles
=======
def can_player_move(y, x, obstacles_letters, board):
    return board[y][x] not in obstacles_letters
>>>>>>> Stashed changes

def move_by(y, x, y_change, x_change):
    y += y_change
    x += x_change

    return y, x

<<<<<<< Updated upstream
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
=======

def main():
    """Handle whole game."""
>>>>>>> Stashed changes
    os.system("clear")
    read_welcome_screen_file()
    x_hero = 1  #starting position of player
    y_hero = 1
    dutifulness = 100
    lives = 3
<<<<<<< Updated upstream
    board = create_board('board.csv')
    previous_sign = board[y_hero][x_hero]
=======
    board = create_board()
    input_key = getch()
>>>>>>> Stashed changes

    obstacles = ["X", "_", "|", "♞", "/"]
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

<<<<<<< Updated upstream
        input_key = getch()
        x_diff, y_diff = control_position(input_key)
        board[y_hero][x_hero] = previous_sign

        if is_move_possible(y_hero + y_diff, x_hero + x_diff, obstacles, board):
            y_hero, x_hero = move_by(y_hero, x_hero, y_diff, x_diff)

        if is_touching_horse(board[y_hero + y_diff][x_hero + x_diff], horse) and not is_key_in_inventory(key, added_items):
=======
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
>>>>>>> Stashed changes
            added_items.append(key)
            add_to_inventory(inventory, added_items)
        elif board[y_hero_new][x_hero_new] in table_elements and note not in added_items and key in inventory:
            added_items.append(note)
            add_to_inventory(inventory, added_items)

<<<<<<< Updated upstream
        if is_touching_blood(board[y_hero + y_diff][x_hero + x_diff], blood):
            dutifulness = subtract_dutifulness(dutifulness)

        if is_touching_door(board[y_hero + y_diff][x_hero + x_diff], door) and is_door_closed(obstacles, door) and is_key_in_inventory(key, added_items):
            obstacles.remove(door)
            return dutifulness, lives, inventory
=======
        if board[y_hero_new][x_hero_new] == blood:
            dutifulness = subtract_dutifulness(dutifulness)

        if board[y_hero_new][x_hero_new] == door and door in obstacles_letters and key in inventory:
            obstacles_letters.remove(door)


>>>>>>> Stashed changes

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
