def is_touching(position_on_board, item):
    return position_on_board == item

def is_item_in_inventory(item, inventory):
    return item in inventory

def is_door_closed(obstacles, door):
    return door in obstacles

def are_all_twanas_in_inventory(inventory):
    return inventory["twanas"] == 9

def is_taking_item(position_on_board, item_place, item, inventory):
    return is_touching(position_on_board, item_place) and not is_item_in_inventory(item, inventory)

def are_items_in_inventory(first_item, second_item, inventory):
    return is_item_in_inventory(first_item, inventory) and is_item_in_inventory(second_item, inventory)

def is_item_and_all_twanas_in_inventory(item, inventory):
    return is_item_in_inventory(item, inventory) and are_all_twanas_in_inventory(inventory)

def is_entering_door(position_on_board, item_place, item, inventory):
    return is_touching(position_on_board, item_place) and not is_item_in_inventory(item, inventory)
