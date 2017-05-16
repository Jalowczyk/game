from collections import OrderedDict
def print_graphical_user_interface(inventory, dutifulness, lives):
    """Displays inventory in particular order."""

    #Finds the longest word by counting letters of every word in inventory.
    the_longest_word = (max(map(len, inventory)))

    print("{} {:>25} {}".format("Inventory:", "Dutifulness:", dutifulness))
    print("-" * (9 + the_longest_word), end ="")
    print("{:>11} {}".format("Lives:", lives))
    #Formats table width to be as long as the longest item.
    print("{:>8} {:>{width}}".format('count', 'item name',
        width = the_longest_word))


    #OrderedDict makes a dictionary-like object that keeps keys in insertion
    #order. OrderedDict is list of tuples (function d.items() - key, value).
    #The key argument for sorted allows to define specific function (lambda
    #- mini function) during sorting. In this example we're sorting by 1-st
    #element of tuple (so it's value of OrderedDict).
    for item in OrderedDict(sorted(inventory.items(), key=lambda t: t[1],
    reverse = True)):
        print("{:>8} {:>{width}}".format(inventory[item], item,
            width = the_longest_word))

    print("-" * (9 + the_longest_word))
    print("Total number of items: ", sum(inventory.values()))

def add_to_inventory(inventory, added_items):
    """Adds to the inventory dictionary a list of items from added_items."""

    for item in added_items:
        if item in inventory:
            inventory[item] += 1
        else:
            inventory[item] = 1

    return inventory

def subtract_dutifulness(dutifulness):

    dutifulness -= 20

    return dutifulness

def print_first_level_description():

    print("\nDESCRIPTION BLAHBLAHBLAH")

def print_second_level_description():

    print("\nSECOND LEVEL OMG")
