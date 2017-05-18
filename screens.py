import csv

def print_screen(filename):
    screen_file = open(filename, 'r')
    screen = []
    for line in screen_file:
        line = list(line[:-1])
        screen.append(line)

    screen_file.close()

    for row in screen:
        for sign in row:
            print(sign, end="")
        print('')

print_screen("welcome_screen.csv")

def choose_character():
    hero_number_chosen_by_user = ""
    user_correct_answer = ["1", "2"]

    while hero_number_chosen_by_user not in user_correct_answer:
        hero_number_chosen_by_user = input("\nEnter 1 or 2 to choose your character. ")

    return hero_number_chosen_by_user
