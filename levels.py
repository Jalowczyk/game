import sys, tty, termios, os, csv

def first_level():
    """Handle whole game."""
    os.system("clear")
    read_welcome_screen_file()
    x_hero = 1  #starting position of player
    y_hero = 1
    dutifulness = 100
    lives = 3
    board = create_board()

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

        elif input_key == "q":
            sys.exit()

        board = create_board()
        insert_player(board, y_hero, x_hero)
        print_board(board)
        print_graphical_user_interface(inventory, dutifulness, lives)
        print_description()
