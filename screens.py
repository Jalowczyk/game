import csv


def read_welcome_screen_file():
    welcome_screen_file = open('welcome_screen.csv', 'r')
    reader_welcome_screen = csv.reader(welcome_screen_file, delimiter = "#")
    welcome_screen = list(reader_welcome_screen)
    welcome_screen_file.close()

    for line in welcome_screen:
        print(*line)


def read_note1():
    note1_file = open('note1.csv', 'r')
    reader_note1 = csv.reader(note1_file, delimiter = "#")
    note1 = list(reader_note1)
    note1_file.close()

    for line in note1:
        print(*line)
