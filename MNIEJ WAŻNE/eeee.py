#import random

#print("----------------------------")
#print("------ Dice Throwing -------")
#print("----------------------------")
#continuation = True


#def menu():
 #   print("1 - Drawing ")
  #  print("2 - Quit")


#def throw():
 #   DiceThrow = random.randrange(1, 7)  # return an int, one of 1,2,3,4,5,6
  #  print(DiceThrow)


#while continuation:
 #   menu()
  #  operation = input("What will you choose ? - ")
   # if operation == "1":
    #    print(throw())
    #elif operation == "2":
     #   continuation = False
    #else:
     #   print(" You choosed wrong number or letter !")



#import random
#print("----------------------------")
#print("------ Dice Throwing -------")
#print("----------------------------")
#continuation = True

#def menu():
 #   print(" ")
  #  print("1 - Drawing ")
   # print("q - Quit")

#def throw():
 #   DiceThrow = random.randrange(1, 7)  # return an int, one of 1,2,3,4,5,6
  #  print(" ")
   # return DiceThrow

#while continuation :
 #   menu()
  #  operation = input("What will you choose ? ")
   # if operation == "1":
    # print(throw())
    #if DiceThrow == "1":
     #print("Ala")
    #elif operation == "q":
     # continuation = False
    #else:
     # print(" You choosed wrong number or letter !")


#import random

#def throw():
 #   Dicethrow = random.randrange(1, 4)  # return an int, one of 1,2,3,4,5,6
  #  return Dicethrow


#if throw() == 1:
 #print("Ala")
#elif throw() == 2:
 #print("Ikola")
#elif throw() == 3:
 #print("Yoda")

#print(throw())

import random

def throw():
    Dicethrow = random.randrange(1, 7)  # return one of 1,2,3
    return Dicethrow

res = throw()

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

