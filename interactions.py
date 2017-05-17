def is_touching(position_on_board, item):
    return position_on_board == item

def is_door_key_in_inventory(door_key, added_items):
    return door_key in added_items

def is_note_in_inventory(note, added_items):
    return note in added_items

def is_door_closed(obstacles, door):
    return door in obstacles

def is_pickaxe_in_inventory(inventory, pickaxe):
    return pickaxe in inventory

def is_scissors_in_inventory(inventory, scissors):
    return scissors in inventory

def are_all_twanas_in_inventory(inventory):
    return inventory["twanas"] == 9

def is_record_in_inventory(inventory, record):
    return record in inventory
