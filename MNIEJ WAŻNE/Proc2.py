#import random
#print("----------------------------")
#print("----- Losowanie Kostką -----")
#print("----------------------------")
#kontynuacja = True
#def menu():
#    print("1 - Losuj ")
#    print("2 - Wyjście")
#
#def rzut():
#    RzutKostką = random.randrange(1, 7)  # return an int, one of 1,2,3,4,5,6
#    print(RzutKostką)
#
#while kontynuacja :
#    menu()
#    operacja = input("Co wybierzesz ? - ")
#    if operacja == "1": print(rzut())
#    elif operacja == "2": kontynuacja = False
#    else : print(" Wybrano błędną liczbę lub literę !")

import random

print("----------------------------")
print("------ Dice Throwing -------")
print("----------------------------")
continuation = True


def menu():
    print("1 - Drawing ")
    print("2 - Quit")


def throw():
    DiceThrow = random.randrange(1, 7)  # return an int, one of 1,2,3,4,5,6
    print(DiceThrow)


while continuation:
    menu()
    operation = input("What will you choose ? - ")
    if operation == "1":
        print(throw())
    elif operation == "2":
        continuation = False
    else:
        print(" You choosed wrong number or letter !")

#proba = random.random()
#print(proba)



#a = input(" Długość Boku : ")
#b = float(a)
#wynik = float(b)*float(b)
#wynik2 = float(b)*4
#print("Pole to : ",wynik," Obwód to : ",wynik2)


