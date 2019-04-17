
# -*- coding: utf-8 -*-
import math

print("Program do liczenia pól figur geometrycznych")
print("Wprowadż 1 aby wybrać kwadtrat, 2 aby wybrać prostokąt itd.")
cont = True

def menu():
    print("1 - kwadrat")
    print("2 - prostokąt")
    print("3 - koło")
    print("4 - trójkąt")


def kwadrat():
    print('    Wybrałeś kwadrat    ')
    a = input(" Długość Boku : ")
    b = float(a)
    wynik = float(b)*float(b)
    wynik2 = float(b)*4
    print("Pole to : ",wynik," Obwód to : ",wynik2)
    menu()


def prostokat():
    print('    Wybrałes Prostokąt    ')
    a = input("Pierwszy Bok : ")
    b = input("Drugi Bok : ")
    wynik = float(a)*float(b)
    wynik2 = float(a)*2+float(b)*2
    print("Pole to : ",wynik," Obwód to : ",wynik2)
    menu()

def kolo():
    print('    Wybrałes Koło    ')
    a = input("Promień : ")
    wynik = float(a)* float(3.141592)**2
    wynik2 = float(a)* float(3.141592)*2
    print("Pole to : ",wynik," Obwód to : ",wynik2)
    menu()

def trojkat():
    print('    Wybrałeś Trójkąt   ')
    a = input("Pierwszy Bok : ")
    b = input("Drugi Bok : ")
    c = input("Trzeci Bok : ")
    a1 = float(a)
    b1 = float(b)
    c1 = float(c)
    wynik = math.sqrt((a1+b1+c1)*(a1+b1-c1)*(a1-b1+c1)*(-a1+b1+c1))
    wynik2 = wynik/4
    print(wynik2)


while cont:
    menu()
    operacja = input("Co wybierzesz ? ")
    if operacja== 1 : kwadrat()
    elif operacja== 2 : prostokat()
    elif operacja== 3 : kolo()
    elif operacja== 4 : trojkat()

    operacja2 = input("Kontynuować program? [tak/nie]")
    if operacja2 == "nie": cont = False
