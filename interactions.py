def is_door_key_in_inventory(door_key, added_items):
    return door_key in added_items

def is_touching_box(position_on_board, box):
    return position_on_board == box

def is_touching_table(position_on_board, table_symbol):
    return position_on_board == table_symbol

def is_note_in_inventory(note, added_items):
    return note in added_items

def is_touching_blood(position_on_board, blood):
    return position_on_board == blood

def is_touching_door(position_on_board, door):
    return position_on_board == door

def is_door_closed(obstacles, door):
    return door in obstacles

def is_touching_twanas(position_on_board, twanas_symbol):
    return position_on_board == twanas_symbol

def is_touching_pickaxe(position_on_board, pickaxe_symbol):
    return position_on_board == pickaxe_symbol

def is_touching_rock(position_on_board, rock):
    return position_on_board == rock

def is_pickaxe_in_inventory(inventory, pickaxe):
    return pickaxe in inventory

def is_scissors_in_inventory(inventory, scissors):
    return scissors in inventory

def is_touching_scissors(position_on_board, scissors_symbol):
    return position_on_board == scissors_symbol

def are_all_twanas_in_inventory(inventory):
    return inventory["twanas"] == 9

def is_touching_answerphone(position_on_board, answerphone):
    return position_on_board == answerphone

def is_touching_front_door(position_on_board, front_door):
    return position_on_board == front_door

def is_record_in_inventory(inventory, record):
    return record in inventory
