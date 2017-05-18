riddles = {"1": 'What police officer should carries with himself?',
            "2": 'What  you should put before gather a evidence?',
            "3": 'What was a murder weapon?'}
hints = {"1":'LAST TRY: G__' ,
            "2": 'LAST TRY: ___V_',
            "3":'LAST TRY: G__'}
description = print("Time to prove your experience..")
count = 1
wrong = "Lost your chance, sorry!"
good = ("Yes, you are good!")


def riddles1(lives, dutifulness, inwentory):
    print(description)
    riddle = input(riddles["1"])
    answer = "gun"

    while riddle != answer and count <2:
        riddle = input(hints["1"])
        count+=1
        if riddle == answer:
            dutifulness += 20
            lives += 1
            print(good)
        else:
            print(wrong)

def riddles2(lives, dutifulness, inwentory):
    print(description)
    riddle = input(riddles["2"])
    answer = "gloves"

    while riddle != answer and count <2:
        riddle = input(hints["2"])
        count+=1
        if riddle == answer:
            dutifulness += 20
            lives += 1
            print(good)
        else:
            print(wrong)

def riddles3(lives, dutifulness, inwentory):
    print(description)
    riddle = input(riddles["3"])
    answer = "axe"

    while riddle != answer and count <2:
        riddle = input(hints["3"])
        count+=1
        if riddle == answer:
            dutifulness += 20
            lives += 1
            print(good)
        else:
            print(wrong)


'''
from random import randint

def hot_cold_game():
    random_number = []
    while len(random_number) != 3:
        num = randint(0, 9)
        if num not in random_number:
            random_number.append(str(num))

    while True:
        guess_number = input("Well,I think about 3-digits number, digits in, do not repeats,
                                can  you guess? ]:> ")

        while not guess_number.isdigit() or len(guess_number) != 3:
            guess_number = input("3-DIGIT INTEGER, something unclear detective?")

        guess_number = list(guess_number)
        #print (guess_number)

        printing_result = []

        for i, elem in enumerate(guess_number):
            if elem in random_number:
                if elem == random_number[i]:
                    printing_result.insert(0, 'hot')
                else:
                    printing_result.append('warm')

        if not printing_result:
            print ("cold!")

        print (*printing_result)
        if all([i == 'hot' for i in printing_result]):
            print ('Wow! You truly are a detective! :)')
            break
'''
