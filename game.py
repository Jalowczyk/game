import sys, tty, termios, os, csv
from graphical_user_interface import *
from screens import *
from create_board import *
from interactions import *
from riddles import *
from hotcold import *
from highscores import *


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

def print_board_and_insert_player(board, y_hero, x_hero, inventory, dutifulness,
                                  log):
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

def process_first_level(dutifulness, inventory, log):
    """Handle game's first level game."""

    x_hero = 1  #starting position of player
    y_hero = 1
    lives = 3
    log = "Hmm... I'm on the crime scene. \nI need to collect the evidence."
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

    input_key = getch()  #control

    while dutifulness != 0:
        x_diff = 0
        y_diff = 0

        input_key = getch()
        x_diff, y_diff = control_position(input_key)
        board[y_hero][x_hero] = previous_sign

        if is_move_possible(y_hero + y_diff, x_hero + x_diff, obstacles, board):
            y_hero, x_hero = move_by(y_hero, x_hero, y_diff, x_diff)

        if is_taking_item(board[y_hero + y_diff][x_hero + x_diff], box,
                          door_key, inventory):
            add_to_inventory(inventory, door_key)
            log = "Now I can open the door!"

        if is_taking_item(board[y_hero + y_diff][x_hero + x_diff], table_symbol,
                          note, inventory):
            add_to_inventory(inventory, note)
            log = "Note: +48500 000 000 - Michael Brown \nI hear an answering machine from another room..."

        if is_touching(board[y_hero + y_diff][x_hero + x_diff], blood):
            dutifulness = subtract_dutifulness(dutifulness)

        if is_taking_item(board[y_hero + y_diff][x_hero + x_diff], answerphone,
                          record, inventory):
            add_to_inventory(inventory, record)
            log = "Record: Come join us on get-together at my cabin in Nashville!"

        if is_touching(board[y_hero + y_diff][x_hero + x_diff], door):
            if is_item_in_inventory(door_key, inventory):
                board[y_hero + y_diff][x_hero + x_diff] = " "
                log = "There is something lying on the table..."
            else:
                log = "I need to find a key!"

        if is_touching(board[y_hero + y_diff][x_hero + x_diff], front_door):
            if are_items_in_inventory(note, record, inventory):
                dutifulness = riddle(dutifulness, "1")
                return dutifulness, inventory, log

        if input_key == "q":
            sys.exit()

        previous_sign = board[y_hero][x_hero]
        print_board_and_insert_player(board, y_hero, x_hero, inventory,
                                      dutifulness, log)

    if dutifulness == 0:
        os.system("clear")
        print_screen("loose.csv")
        sys.exit()

def process_second_level(dutifulness, inventory, log):
    """Handle game's second level game."""
    os.system("clear")
    x_hero = 1  #starting position of player
    y_hero = 1
    board = create_board("forest.csv")
    previous_sign = board[y_hero][x_hero]
    log = "I need to collect these strange crosses, they can be evidence..."

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

    while dutifulness != 0:
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
                log = "A bloog-stained scissors? It can be a murder weapon..."
            else:
                log = "I need to find a tool to destroy this rock..."

        if is_taking_item(board[y_hero + y_diff][x_hero + x_diff],
                          scissors_symbol, scissors, inventory):
            board[y_hero + y_diff][x_hero + x_diff] = " "
            add_to_inventory(inventory, scissors)
            log = "I need to go back to police station now."

        if is_touching(board[y_hero + y_diff][x_hero + x_diff], enter):
            if is_item_and_all_twanas_in_inventory(scissors, inventory):
                return dutifulness, inventory, log

        previous_sign = board[y_hero][x_hero]
        print_board_and_insert_player(board, y_hero, x_hero, inventory,
                                      dutifulness,  log)

    if dutifulness == 0:
        os.system("clear")
        print_screen("loose.csv")
        sys.exit()


def process_third_level(dutifulness,  inventory, log):
    """Handle game's first level game."""
    os.system("clear")
    x_hero = 1  #starting position of player
    y_hero = 1
    board = create_board('city.csv')
    previous_sign = board[y_hero][x_hero]
    log = "This city is mad! \nI need to find a way to the police station..."

    obstacles = ["▓", "▆", "⛔", "@", "⟧"]
    gate = "⛔"
    friend = "@"
    greenery = "☘"
    gate_key = "gate key"
    police_station_door = "⟧"
    greenery = "☘"

    input_key = getch()  #control

    while dutifulness != 0:
        x_diff = 0
        y_diff = 0

        input_key = getch()
        x_diff, y_diff = control_position(input_key)
        board[y_hero][x_hero] = previous_sign

        if is_move_possible(y_hero + y_diff, x_hero + x_diff, obstacles, board):
            y_hero, x_hero = move_by(y_hero, x_hero, y_diff, x_diff)

        if is_taking_item(board[y_hero + y_diff][x_hero + x_diff], friend,
                          gate_key, inventory):
            add_to_inventory(inventory, gate_key)
            log = "Now I can enter the gate!"

        if is_touching(board[y_hero + y_diff][x_hero + x_diff], greenery):
            dutifulness = subtract_dutifulness(dutifulness)

        if is_touching(board[y_hero + y_diff][x_hero + x_diff], gate):
            if is_item_in_inventory(gate_key, inventory):
                board[y_hero + y_diff][x_hero + x_diff] = " "
                log = "Ok, let's go to police station!"
            else:
                log = "I need to find Michael to borrow a key from him."

        if is_touching(board[y_hero + y_diff][x_hero + x_diff],
                        police_station_door):
            dutifulness = riddle(dutifulness, "3")
            return dutifulness, inventory, log

        if input_key == "q":
            sys.exit()

        previous_sign = board[y_hero][x_hero]
        print_board_and_insert_player(board, y_hero, x_hero, inventory,
                                      dutifulness, log)

    if dutifulness == 0:
        os.system("clear")
        print_screen("loose.csv")
        sys.exit()

def process_fourth_level(dutifulness, inventory, log):
    """Handle game's third level game."""
    os.system("clear")
    x_hero = 1  #starting position of player
    y_hero = 1
    board = create_board("police_station.csv")
    previous_sign = board[y_hero][x_hero]
    log = "Now I need to go to my office."

    obstacles = ["☎", "⚿", "▆", "▓", "⟧", "@", "▯"]
    office_key_symbol = "⚿"
    office_key = "key to office"
    door = "⟧"
    telephone = "☎"
    front_door = "▯"

    input_key = getch()  #control

    while dutifulness != 0:
        x_diff = 0
        y_diff = 0

        input_key = getch()
        x_diff, y_diff = control_position(input_key)
        board[y_hero][x_hero] = previous_sign

        if is_move_possible(y_hero + y_diff, x_hero + x_diff, obstacles, board):
            y_hero, x_hero = move_by(y_hero, x_hero, y_diff, x_diff)

        if is_touching(board[y_hero + y_diff][x_hero + x_diff], office_key_symbol):
            add_to_inventory(inventory, office_key)
            log = "Now I can open the office door."

        if is_touching(board[y_hero + y_diff][x_hero + x_diff], door):
            if is_item_in_inventory(office_key, inventory):
                board[y_hero + y_diff][x_hero + x_diff] = " "
                log = "Telephone is ringing, I need to pick it up!"
            else:
                log = "I need a key."

        if is_touching(board[y_hero + y_diff][x_hero + x_diff], telephone):
            log = "Boss: Senior investigator, come to my office, now."

        if is_touching(board[y_hero + y_diff][x_hero + x_diff], front_door):
            dutifulness = riddle(dutifulness, "4")
            return dutifulness, inventory, log

        previous_sign = board[y_hero][x_hero]
        print_board_and_insert_player(board, y_hero, x_hero, inventory,
                                    dutifulness, log)


def process_fifth_level(dutifulness, inventory, log):
    """Handle game's second level game."""
    os.system("clear")
    x_hero = 1  #starting position of player
    y_hero = 1
    board = create_board("boss.csv")
    previous_sign = board[y_hero][x_hero]
    log = "OMG I'm so anxious, what does the boss want?"

    obstacles = ["▓"]
    clock = "⏰"

    input_key = getch()  #control

    while dutifulness != 0:
        x_diff = 0
        y_diff = 0

        input_key = getch()
        x_diff, y_diff = control_position(input_key)
        board[y_hero][x_hero] = previous_sign

        if is_move_possible(y_hero + y_diff, x_hero + x_diff, obstacles, board):
            y_hero, x_hero = move_by(y_hero, x_hero, y_diff, x_diff)

        if is_touching(board[y_hero + y_diff][x_hero + x_diff], clock):
            hot_and_cold_game()
            return dutifulness, inventory, log

        previous_sign = board[y_hero][x_hero]
        print_board_and_insert_player(board, y_hero, x_hero, inventory,
                                      dutifulness, log)

def main():
    os.system("clear")
    print_screen("welcome_screen.csv")
    print_screen("how_to_play.csv")
    print_screen("choose_your_hero.csv")

    hero_number_chosen_by_user = choose_character()

    if hero_number_chosen_by_user == "1":
        dutifulness = 5000

    if hero_number_chosen_by_user == "2":
        dutifulness = 60

    log = []
    inventory = {"gun": 1}

    dutifulness, inventory, log = process_first_level(dutifulness, inventory, log)
    dutifulness, inventory, log = process_second_level(dutifulness, inventory, log)
    dutifulness, inventory, log = process_third_level(dutifulness, inventory, log)
    dutifulness, inventory, log = process_fourth_level(dutifulness, inventory, log)
    dutifulness, inventory, log = process_fifth_level(dutifulness, inventory, log)

    os.system("clear")
    print_screen("won.csv")

    user_name = input("\nPut your name to save your score to highscores! ")

    save_to_highscores(dutifulness, user_name)
    print_highscores()

if __name__ == "__main__":
    main()
