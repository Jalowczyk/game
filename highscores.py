import csv
def highs():
    name = "hihi"
    dutifilness = 50
    highscores_list = [name, dutifilness]

    with open('highscores.csv', 'a')  as highscores_file:       # tworze, zapisuje wyniki
        writer =  csv.writer(highscores_file)
        writer.writerow(highscores_list)
        highscores_file.close()

highscores_list = []
with open('highscores.csv', 'r')  as highscores_file:       # eksport
    reader =  csv.reader(highscores_file, delimiter = ",")

    for line in reader:
        highscores_list.append(line)
    highscores_file.close()
print(highscores_list)

for score in sorted(highscores_list, key = lambda t: t[1], reverse = True):# key po czym sortujemy
    print(*score)
