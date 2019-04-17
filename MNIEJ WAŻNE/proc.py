
# -*- coding: utf-8 -*-#
print("Program do liczenia pól figur geometrycznych")
print("Wprowadż 1 aby wybrać kwadtrat, 2 aby wybrać prostokąt itd.")
cont = True

def menu():
    print("1 - Proc")
    print("2 - Deltoid")

def percentage(percent, whole):
    return (percent * whole) / 100.0


def proc():
    print("")
    a = input("Wybierz liczbę : ")
    a2 = input("Procent z liczby : ")
    b = float(a)
    b3 = float(a2) / 100
    wynik = float(b) * float(b3)
    print("Wartość procentu : ", wynik)

def deltoid():
    print('    Wybrałeś Deltoid   ')
    a = input(" Długość Przekątnej E : ")
    b = input(" Długość Przekątnej F : ")
    c = input(" Pierwszy Bok : ")
    d = input(" Drugi Bok : " )
    wynik = (float(a)*float(b))/2
    wynik3 = float(c)*2 + float(d)*2
    print("Pole wynosi : ", wynik,"Obwód wynosi: ", wynik3)

while cont:
    menu()
    operacja = input("Co wybierzesz ? ")
    if operacja == "1" : proc()
    elif operacja == "2" : deltoid()
    else: print("Wybrałeś nieprawidlową cyfrę lub literę!")

    operacja2 = input("Kontynuować program? [tak/nie] ")
    if operacja2 == "nie": cont = False
    elif operacja2 == "tak": cont = True
    else: print("Wybrałeś nieprawidlową cyfrę lub literę!")