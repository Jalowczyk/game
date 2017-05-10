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
    board = create_board()
    input_key = getch()
    obstacles_letters = ["X", "_", "|", "♞"]
    inventory = {"purple key": 2, "dope": 3}
    added_items = []
    key_giver = "♞"
    table_elements = ["_", "|"]
    note = "note"
    key = "key"

    while input_key != "q":
        diff_x = 0
        diff_y = 0

        input_key = getch()  #control
        if input_key == "d":
            diff_x = 1
            diff_y = 0
        elif input_key == "a":
            diff_x = -1
            diff_y = 0
        elif input_key == "s":
            diff_x = 0
            diff_y = 1
        elif input_key == "w":
            diff_x = 0
            diff_y = -1

        y_hero_new = y_hero + diff_y
        x_hero_new = x_hero + diff_x
        if can_player_move(y_hero_new, x_hero_new, obstacles_letters, board):
            y_hero, x_hero = move_by(y_hero, x_hero, diff_y, diff_x)
        elif board[y_hero_new][x_hero_new] == key_giver and key not in added_items:
            added_items.append(key)
            add_to_inventory(inventory, added_items)
        elif board[y_hero_new][x_hero_new] in table_elements and note not in added_items and key in inventory:
            added_items.append(note)
            add_to_inventory(inventory, added_items)

        elif input_key == "q":
            sys.exit()

        board = create_board()
        insert_player(board, y_hero, x_hero)
        print_board(board)
        print_table(inventory)


main()
