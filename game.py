import sys, tty, termios, os, csv
from inventory import print_table, add_to_inventory
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


def main():
    """Handle whole game."""
    os. system("clear")
    read_welcome_screen_file()
    x_hero = 1  #starting position of player
    y_hero = 1
    board = create_board()
    x = getch()
    obstacles_letters = ["X", "{", "}", "_", "|"]
    inventory = {"purple key": 2, "dope": 3}
    added_items = []

    while x != "q":

        x = getch() #control
        if x == "d":
            if board[y_hero][x_hero + 1] not in obstacles_letters:
                x_hero += 1
            elif board[y_hero][x_hero + 1] in ["{", "}"] and "key" not in added_items:
                added_items.append("key")
                add_to_inventory(inventory, added_items)
            elif board[y_hero][x_hero + 1] in ["_", "|"] and "note" not in added_items and "key" in inventory:
                    added_items.append("note")
                    add_to_inventory(inventory, added_items)
        elif x == "a":
            if board[y_hero][x_hero - 1] not in obstacles_letters:
                x_hero -= 1
            elif board[y_hero][x_hero - 1] in ["{", "}"] and "key" not in added_items:
                added_items.append("key")
                add_to_inventory(inventory, added_items)
            elif board[y_hero][x_hero - 1] in ["_", "|"] and "note" not in added_items and "key" in inventory:
                added_items.append("note")
                add_to_inventory(inventory, added_items)
        elif x == "s":
            if board[y_hero + 1][x_hero] not in obstacles_letters:
                y_hero += 1
            elif board[y_hero + 1][x_hero] in ["{", "}"] and "key" not in added_items:
                added_items.append("key")
                add_to_inventory(inventory, added_items)
            elif board[y_hero + 1][x_hero] in ["_", "|"] and "note" not in added_items and "key" in inventory:
                added_items.append("note")
                add_to_inventory(inventory, added_items)
        elif x == "w":
            if board[y_hero - 1][x_hero] not in obstacles_letters:
                y_hero -= 1
            elif board[y_hero - 1][x_hero] in ["{", "}"] and "key" not in added_items:
                added_items.append("key")
                add_to_inventory(inventory, added_items)
            elif board[y_hero - 1][x_hero] in ["_", "|"] and "note" not in added_items and "key" in inventory:
                added_items.append("note")
                add_to_inventory(inventory, added_items)
        elif x == "q":
            sys.exit()

        board = create_board()
        insert_player(board, y_hero, x_hero)
        print_board(board)
        print_table(inventory)


main()
