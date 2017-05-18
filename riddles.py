riddles = {"1": '\nWhat police officer should carries with himself? ',
            "2": '\nWhat you should put before gather a evidence? ',
            "3": '\nDo you understand that not listening to higher ranks lead to you being permanently discharged? ',
            "4": "\nWhat's the name of the U.S. Navy's primary special operations force? "}
hints = {"1":'\nIt starts with letter "g"... ' ,
            "2": '\nIt starts with letter "g"... ',
            "3":'\nIt starts with letter "y"... ',
            "4": '\nIt starts with letter "s"... '}

answer_dic = {"1": "gun", "2": "gloves","3": "yes", "4": "seals"}

red = '\033[93m'
white = '\033[0m'

def riddle(dutifulness, number):
    print(red, "\nBoss: before you go, you should prove your dutifulness...",
        "\nIf you are correct, you will earn +20 dutifulness,",
        "\nif not... you will lose -10 dutifulness for a try.", white)
    riddle = input(riddles[number])
    answer = answer_dic[number]
    count = 0
    if riddle.lower() == answer:
        dutifulness += 20
        return dutifulness

    while riddle != answer and count <2:
        riddle = input(hints[number])
        count+=1
        if riddle.lower() == answer:
            dutifulness += 20

        else:
            dutifulness -= 10

    return dutifulness
