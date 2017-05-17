import csv

def read_welcome_screen_file():
    welcome_screen_file = open('welcome_screen.csv', 'r')
    reader_welcome_screen = csv.reader(welcome_screen_file, delimiter = "#")
    welcome_screen = list(reader_welcome_screen)
    welcome_screen_file.close()

    for line in welcome_screen:
        print(*line)
