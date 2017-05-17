def is_touching(position_on_board, item):
    return position_on_board == item

def is_item_in_inventory(item, inventory):
    return item in inventory

def is_door_closed(obstacles, door):
    return door in obstacles

def are_all_twanas_in_inventory(inventory):
    return inventory["twanas"] == 9
