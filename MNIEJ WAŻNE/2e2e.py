import random
print("----------------------------")
print("----- Losowanie Kostką -----")
print("----------------------------")
kontynuacja = True
def menu():
    print("1 - Losuj ")
    print("2 - Wyjście")

def rzut():
    RzutKostką = random.randrange(1, 7)  # return an int, one of 1,2,3,4,5,6
    print(RzutKostką)

while kontynuacja :
    menu()
    operacja = input("Co wybierzesz ? - ")
    if operacja == "1": print(rzut())
    elif operacja == "2": kontynuacja = False
    else : print(" Wybrano błędną liczbę lub literę !")


#proba = random.random()
#print(proba)



#a = input(" Długość Boku : ")
#b = float(a)
#wynik = float(b)*float(b)
#wynik2 = float(b)*4
#print("Pole to : ",wynik," Obwód to : ",wynik2)


