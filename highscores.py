import csv

def save_to_highscores(dutifulness, user_name):
    highscores_list = [user_name, dutifulness]

    with open('highscores.csv', 'a')  as highscores_file:
        writer =  csv.writer(highscores_file)
        writer.writerow(highscores_list)
        highscores_file.close()

def print_highscores():
    highscores_list = []
    with open('highscores.csv', 'r') as highscores_file:
        reader =  csv.reader(highscores_file, delimiter = ",")

        for line in reader:
            highscores_list.append(line)
        highscores_file.close()

    list_of_names = []
    for sublist in highscores_list:
        list_of_names.append(sublist[0])

    length_of_longest_word = (max(map(len, list_of_names)))

    print("{} {:>{width}}".format("\nName:", "Score:", width = length_of_longest_word))
    print("-" * (6 + length_of_longest_word))

    for score in sorted(highscores_list, key = lambda t: t[1], reverse = True):
        print("{:{width}} {}".format(score[0], score[1], width = length_of_longest_word))

    print("-" * (6 + length_of_longest_word))
