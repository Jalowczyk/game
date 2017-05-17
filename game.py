#-*- coding: utf-8 -*-
import sys, tty, termios, os, csv
from graphical_user_interface import *
from screens import *
from create_board import *
from interactions import *


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

def print_board_and_insert_player(board, y_hero, x_hero, inventory, dutifulness, lives):
    insert_player(board, y_hero, x_hero)
    print_board(board)
    print_graphical_user_interface(inventory, dutifulness, lives)

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
    note = "note"
    door_key = "door key"

    inventory = {"gun": 1, "bullets": 2}


    input_key = getch()  #control

    while input_key != "q":
        x_diff = 0
        y_diff = 0

        input_key = getch()
        x_diff, y_diff = control_position(input_key)
        board[y_hero][x_hero] = previous_sign

        if is_move_possible(y_hero + y_diff, x_hero + x_diff, obstacles, board):
            y_hero, x_hero = move_by(y_hero, x_hero, y_diff, x_diff)

        if is_touching(board[y_hero + y_diff][x_hero + x_diff], box) and not is_item_in_inventory(door_key, inventory):
            add_to_inventory(inventory, door_key)

        if is_touching(board[y_hero + y_diff][x_hero + x_diff], table_symbol) and not is_item_in_inventory(note, inventory):
            add_to_inventory(inventory, note)

        if is_touching(board[y_hero + y_diff][x_hero + x_diff], blood):
            dutifulness = subtract_dutifulness(dutifulness)

        if is_touching(board[y_hero + y_diff][x_hero + x_diff], answerphone) and not is_item_in_inventory(record, inventory):
            add_to_inventory(inventory, record)

        if is_touching(board[y_hero + y_diff][x_hero + x_diff], door) and is_item_in_inventory(door_key, inventory):
            board[y_hero + y_diff][x_hero + x_diff] = " "

        if is_touching(board[y_hero + y_diff][x_hero + x_diff], front_door) and is_item_in_inventory(note, inventory) and is_item_in_inventory(record, inventory):
            return dutifulness, lives, inventory

        if input_key == "q":
            sys.exit()

        previous_sign = board[y_hero][x_hero]
        print_board_and_insert_player(board, y_hero, x_hero, inventory, dutifulness, lives)
        print_first_level_description()

def second_level(dutifulness, lives, inventory):
    """Handle game's second level game."""
    os.system("clear")
    x_hero = 1  #starting position of player
    y_hero = 1
    board = create_board("forest.csv")
    previous_sign = board[y_hero][x_hero]

    obstacles = ["▓", "☘", "༊", "✀", "⛏", "༼"]
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

        if is_touching(board[y_hero + y_diff][x_hero + x_diff], blood):
            dutifulness = subtract_dutifulness(dutifulness)

        if is_touching(board[y_hero + y_diff][x_hero + x_diff], twanas_symbol):
            board[y_hero + y_diff][x_hero + x_diff] = " "
            add_to_inventory(inventory, twanas)

        if is_touching(board[y_hero + y_diff][x_hero + x_diff], pickaxe_symbol):
            board[y_hero + y_diff][x_hero + x_diff] = " "
            add_to_inventory(inventory, pickaxe)

        if is_touching(board[y_hero + y_diff][x_hero + x_diff], rock) and is_item_in_inventory(pickaxe, inventory):
            board[y_hero + y_diff][x_hero + x_diff] = " "
            obstacles.remove(rock)

        if is_touching(board[y_hero + y_diff][x_hero + x_diff], scissors_symbol) and not is_item_in_inventory(scissors, inventory):
            board[y_hero + y_diff][x_hero + x_diff] = " "
            add_to_inventory(inventory, scissors)

        if is_item_in_inventory(scissors, inventory) and are_all_twanas_in_inventory(inventory):
            return dutifulness, lives, inventory

        previous_sign = board[y_hero][x_hero]
        print_board_and_insert_player(board, y_hero, x_hero, inventory, dutifulness, lives)
        print_second_level_description()

def main():
    dutifulness, lives, inventory = first_level()
    second_level(dutifulness, lives, inventory)

main()
