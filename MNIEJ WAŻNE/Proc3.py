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


import random

def throw():
    Dicethrow = random.randrange(1, 4)  # return an int, one of 1,2,3,4,5,6
    return Dicethrow


if throw() == 1:
 print("Ala")
elif throw() == 2:
 print("Ikola")
elif throw() == 3:
 print("Yoda")

#print(throw())