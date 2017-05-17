def is_key_in_inventory(key, added_items):
    return key in added_items

def is_touching_horse(position_on_board, horse):
    return position_on_board == horse

def is_touching_table(position_on_board, table_elements):
    return position_on_board in table_elements

def is_note_in_inventory(note, added_items):
    return note in added_items

def is_touching_blood(position_on_board, blood):
    return position_on_board == blood

def is_touching_door(position_on_board, door):
    return position_on_board == door

def is_door_closed(obstacles, door):
    return door in obstacles

def is_touching_twanas(position_on_board, twanas_list):
    return position_on_board in twanas_list
