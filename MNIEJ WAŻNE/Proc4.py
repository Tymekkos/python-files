

#import random







#def throw():
 #   DiceThrow = random.randrange(1, 7)  # return an int, one of 1,2,3,4,5,6
  #  print(DiceThrow)











import random

print("----------------------------")
print("------ Dice Throwing -------")
print("----------------------------")
continuation = True

def menu():
    print("1 - Drawing ")
    print("2 - Quit")

menu()
operation = input("What will you choose ? - ")
while continuation:

    def throw():
        Dicethrow = random.randrange(1, 7)  # return one of 1,2,3
        return Dicethrow

    res = throw()

    if operation == "1":
        if res == 1:
            print("          X  X  X")
            print("1    -    X  O  X")
            print("          X  X  X")
        elif res == 2:
            print("          X  X  X")
            print("2    -    O  X  O")
            print("          X  X  X")
        elif res == 3:
            print("          X  X  O")
            print("3    -    X  O  X")
            print("          O  X  X")
        elif res == 4:
            print("          O  X  O")
            print("4    -    X  X  X")
            print("          O  X  O")
        elif res == 5:
            print("          O  X  O")
            print("5    -    X  O  X")
            print("          O  X  O")
        elif res == 6:
            print("          O  X  O")
            print("6    -    O  X  O")
            print("          O  X  O")
    elif operation == "2":
        continuation = False
    else:
        print(" You choosed wrong number or letter !")
    operation2 = input("Would You like to continue this program? [yes - \"press enter\" / no] ")
    if operation2 == "no":
        continuation = False
    elif operation2 == "":
        continuation = True


#Pozdrawiam

