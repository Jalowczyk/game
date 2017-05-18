import sys, tty, termios, os, csv
from graphical_user_interface import *
from screens import *
from create_board import *
from interactions import *
red = '\033[93m'


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

def print_board_and_insert_player(board, y_hero, x_hero, inventory, dutifulness,  log):
    insert_player(board, y_hero, x_hero)
    print_board(board)
    print_graphical_user_interface(inventory, dutifulness, log)

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
    lives = 3
    dutifulness = 100
    log = "DESCRIPTION ABOUT FIRST LEVEL"
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

    while dutifulness != 0:
        x_diff = 0
        y_diff = 0

        input_key = getch()
        x_diff, y_diff = control_position(input_key)
        board[y_hero][x_hero] = previous_sign

        if is_move_possible(y_hero + y_diff, x_hero + x_diff, obstacles, board):
            y_hero, x_hero = move_by(y_hero, x_hero, y_diff, x_diff)

        if is_touching(board[y_hero + y_diff][x_hero + x_diff], box) and not is_item_in_inventory(door_key, inventory):
            add_to_inventory(inventory, door_key)
            log = "Now I can open the door!"

        if is_touching(board[y_hero + y_diff][x_hero + x_diff], table_symbol) and not is_item_in_inventory(note, inventory):
            add_to_inventory(inventory, note)
            log = "NOTE + I hear an answerphone from the another room..."

        if is_touching(board[y_hero + y_diff][x_hero + x_diff], blood):
            dutifulness = subtract_dutifulness(dutifulness)

        if is_touching(board[y_hero + y_diff][x_hero + x_diff], answerphone) and not is_item_in_inventory(record, inventory):
            add_to_inventory(inventory, record)
            log = "RECORD + So I should go and check if I find something important in forest."

        if is_touching(board[y_hero + y_diff][x_hero + x_diff], door):
            if is_item_in_inventory(door_key, inventory):
                board[y_hero + y_diff][x_hero + x_diff] = " "
                log = "Oh, there is so much blood around the table! \nAnd there is something lying..."
            else:
                log = "I need to find a key!"

        if is_touching(board[y_hero + y_diff][x_hero + x_diff], front_door) and is_item_in_inventory(note, inventory) and is_item_in_inventory(record, inventory):
            return dutifulness,  inventory, log

        if input_key == "q":
            sys.exit()

        previous_sign = board[y_hero][x_hero]
        print_board_and_insert_player(board, y_hero, x_hero, inventory, dutifulness, log)

    if dutifulness == 0:
        log = red + "I have contaminated murder scene... \nI got fired from a police..."
        print_board_and_insert_player(board, y_hero, x_hero, inventory, dutifulness, log)
        sys.exit()

def second_level(dutifulness,  inventory, log):
    """Handle game's second level game."""
    os.system("clear")
    x_hero = 1  #starting position of player
    y_hero = 1
    board = create_board("forest.csv")
    previous_sign = board[y_hero][x_hero]
    log = "DESCRIPTION ABOUT SECOND LEVEL"

    obstacles = ["▓", "☘", "༊", "✀", "⛏", "༼", "▯"]
    blood = "~"
    twanas_symbol = "✞"
    twanas = "twanas"
    pickaxe_symbol = "⛏"
    pickaxe = "pickaxe"
    rock = "༼"
    scissors = "scissors"
    enter = "▯"
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
            log = "Hmmm... pickaxe... I can use it somehow..."

        if is_touching(board[y_hero + y_diff][x_hero + x_diff], rock):
            if is_item_in_inventory(pickaxe, inventory):
                board[y_hero + y_diff][x_hero + x_diff] = " "
                obstacles.remove(rock)
                log = "A bloog-stained scissors? \nIt can be a murder weapon..."
            else:
                log = "I need to find a tool to destroy this rock..."

        if is_touching(board[y_hero + y_diff][x_hero + x_diff], scissors_symbol) and not is_item_in_inventory(scissors, inventory):
            board[y_hero + y_diff][x_hero + x_diff] = " "
            add_to_inventory(inventory, scissors)
            log = "I need to go back to police station now."

        if is_item_in_inventory(scissors, inventory) and are_all_twanas_in_inventory(inventory) and is_touching(board[y_hero + y_diff][x_hero + x_diff], enter):
            return dutifulness,  inventory, log

        previous_sign = board[y_hero][x_hero]
        print_board_and_insert_player(board, y_hero, x_hero, inventory, dutifulness,  log)

def third_level(dutifulness,  inventory, log):
    """Handle game's first level game."""
    os.system("clear")
    x_hero = 1  #starting position of player
    y_hero = 1
    board = create_board('city.csv')
    previous_sign = board[y_hero][x_hero]
    log = "DESCRIPTION ABOUT THIRD LEVEL"

    obstacles = ["▓", "▆", "⛔", "@", "⟧"]
    gate = "⛔"
    friend = "@"
    greenery = "☘"
    gate_key = "gate key"
    police_station_door = "⟧"
    greenery = "☘"

    input_key = getch()  #control

    while input_key != "q":
        x_diff = 0
        y_diff = 0

        input_key = getch()
        x_diff, y_diff = control_position(input_key)
        board[y_hero][x_hero] = previous_sign

        if is_move_possible(y_hero + y_diff, x_hero + x_diff, obstacles, board):
            y_hero, x_hero = move_by(y_hero, x_hero, y_diff, x_diff)

        if is_touching(board[y_hero + y_diff][x_hero + x_diff], friend) and not is_item_in_inventory(gate_key, inventory):
            add_to_inventory(inventory, gate_key)
            log = "Now I can enter the gate!"

        if is_touching(board[y_hero + y_diff][x_hero + x_diff], greenery):
            dutifulness = subtract_dutifulness(dutifulness)

        if is_touching(board[y_hero + y_diff][x_hero + x_diff], gate):
            if is_item_in_inventory(gate_key, inventory):
                board[y_hero + y_diff][x_hero + x_diff] = " "
                log = "Ok, let's go to police station!"
            else:
                log = "Oh It's closed and I forgot a key! \nI need to find Michael to borrow a key from him."
        if is_touching(board[y_hero + y_diff][x_hero + x_diff], police_station_door):
            return dutifulness,  inventory, log

        if input_key == "q":
            sys.exit()

        previous_sign = board[y_hero][x_hero]
        print_board_and_insert_player(board, y_hero, x_hero, inventory, dutifulness,  log)


def fourth_level(dutifulness,  inventory, log):
    """Handle game's third level game."""
    os.system("clear")
    x_hero = 1  #starting position of player
    y_hero = 1
    board = create_board("police_station.csv")
    previous_sign = board[y_hero][x_hero]

    obstacles = ["☎", "⚿", "▆", "▓", "⟧", "@"]
    key_to_office_symbol = "⚿"
    key_to_office = "key to office"
    door = "⟧"
    telephone = "☎"

    input_key = getch()  #control

    while input_key != "q":
        x_diff = 0
        y_diff = 0

        input_key = getch()
        x_diff, y_diff = control_position(input_key)
        board[y_hero][x_hero] = previous_sign

        if is_move_possible(y_hero + y_diff, x_hero + x_diff, obstacles, board):
            y_hero, x_hero = move_by(y_hero, x_hero, y_diff, x_diff)

        if is_touching(board[y_hero + y_diff][x_hero + x_diff], key_to_office_symbol):
            add_to_inventory(inventory, key_to_office)
            log = "Now I can open my office door."

        if is_touching(board[y_hero + y_diff][x_hero + x_diff], door):
            if is_item_in_inventory(key_to_office, inventory):
                board[y_hero + y_diff][x_hero + x_diff] = " "
                log = "Telephone is ringing, I need to pick up!"
            else:
                log = "I need a key."

        if is_touching(board[y_hero + y_diff][x_hero + x_diff], telephone):
            log = "TELEPHONE"

        previous_sign = board[y_hero][x_hero]
        print_board_and_insert_player(board, y_hero, x_hero, inventory, dutifulness,  log)


def main():

        dutifulness, inventory, log = first_level()
        second_level(dutifulness, inventory, log)
        third_level(dutifulness, inventory, log)
        fourth_level(dutifulness, inventory, log)


main()
