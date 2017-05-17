#-*- coding: utf-8 -*-
import sys, tty, termios, os, csv
from graphical_user_interface import *
from screens import *
from create_board import *
from interactions import *
from levels import *

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
    board = create_board('home.csv')
    previous_sign = board[y_hero][x_hero]

    obstacles = ["⟧", "▆", "▓", "ߛ", "☎", "Ր", "♨", "இ", "☘", "□", "▯"]
    table_symbol = "▆"
    door = "⟧"
    box = "ߛ"
    blood = "~"
    answerphone = "□"
    front_door = "▯"
    record = "record"
    inventory = {"gun": 1, "bullets": 2}
    added_items = []


    note = "note"
    door_key = "door key"

    input_key = getch()  #control

    while input_key != "q":
        x_diff = 0
        y_diff = 0

        input_key = getch()
        x_diff, y_diff = control_position(input_key)
        board[y_hero][x_hero] = previous_sign

        if is_move_possible(y_hero + y_diff, x_hero + x_diff, obstacles, board):
            y_hero, x_hero = move_by(y_hero, x_hero, y_diff, x_diff)

        if is_touching_box(board[y_hero + y_diff][x_hero + x_diff], box) and not is_door_key_in_inventory(door_key, added_items):
            added_items.append(door_key)
            add_to_inventory(inventory, added_items)

        if is_touching_table(board[y_hero + y_diff][x_hero + x_diff], table_symbol) and not is_note_in_inventory(note, added_items):
            added_items.append(note)
            add_to_inventory(inventory, added_items)

        if is_touching_blood(board[y_hero + y_diff][x_hero + x_diff], blood):
            dutifulness = subtract_dutifulness(dutifulness)

        if is_touching_answerphone(board[y_hero + y_diff][x_hero + x_diff], answerphone):
            added_items.append(record)
            add_to_inventory(inventory, added_items)

        if is_touching_door(board[y_hero + y_diff][x_hero + x_diff], door) and is_door_closed(obstacles, door) and is_door_key_in_inventory(door_key, added_items):
            board[y_hero + y_diff][x_hero + x_diff] = " "
            obstacles.remove(door)

        if is_touching_front_door(board[y_hero + y_diff][x_hero + x_diff], front_door) and is_note_in_inventory(note, added_items) and is_record_in_inventory(inventory, record):
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
    board = create_board("forest.csv")
    previous_sign = board[y_hero][x_hero]

    obstacles = ["▓", "☘", "༊", "✀", "⛏", "༼"]
    added_items = []
    blood = "~"
    twanas_symbol = "✞"
    twanas = "twanas"
    pickaxe_symbol = "⛏"
    pickaxe = "pickaxe"
    rock = "༼"
    scissors = "scissors"
    scissors_symbol = "✀"

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

        if is_touching_twanas(board[y_hero + y_diff][x_hero + x_diff], twanas_symbol):
            board[y_hero + y_diff][x_hero + x_diff] = " "
            added_items.append(twanas)
            add_to_inventory(inventory, added_items)
            added_items.remove(twanas)

        if is_touching_pickaxe(board[y_hero + y_diff][x_hero + x_diff], pickaxe_symbol):
            board[y_hero + y_diff][x_hero + x_diff] = " "
            added_items.append(pickaxe)
            add_to_inventory(inventory, added_items)

        if is_touching_rock(board[y_hero + y_diff][x_hero + x_diff], rock) and is_pickaxe_in_inventory(inventory, pickaxe):
            board[y_hero + y_diff][x_hero + x_diff] = " "
            obstacles.remove(rock)

        if is_touching_scissors(board[y_hero + y_diff][x_hero + x_diff], scissors_symbol) and not is_scissors_in_inventory(inventory, scissors):
            board[y_hero + y_diff][x_hero + x_diff] = " "
            added_items.append(scissors)
            add_to_inventory(inventory, added_items)

        if is_scissors_in_inventory(inventory, scissors) and are_all_twanas_in_inventory(inventory):
            return dutifulness, lives, inventory

        previous_sign = board[y_hero][x_hero]
        insert_player(board, y_hero, x_hero)
        print_board(board)
        print_graphical_user_interface(inventory, dutifulness, lives)
        print_second_level_description()

def main():
    dutifulness, lives, inventory = first_level()
    second_level(dutifulness, lives, inventory)

main()
