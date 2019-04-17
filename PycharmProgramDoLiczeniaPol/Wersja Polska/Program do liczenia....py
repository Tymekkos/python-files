
# -*- coding: utf-8 -*-
import math

print("Program do liczenia pól figur geometrycznych")
print("Wprowadż 1 aby wybrać kwadtrat, 2 aby wybrać prostokąt itd.")
cont = True

def menu():
    print("1 - Kwadrat")
    print("2 - Prostokąt")
    print("3 - Koło")
    print("4 - Trójkąt")
    print("5 - Romb")
    print("6 - Trapez")
    print("7 - Deltoid")


def kwadrat():
    print('    Wybrałeś Kwadrat    ')
    a = input(" Długość Boku : ")
    b = float(a)
    wynik = float(b)*float(b)
    wynik2 = float(b)*4
    print("Pole to : ",wynik," Obwód to : ",wynik2)



def prostokat():
    print('    Wybrałes Prostokąt    ')
    a = input("Pierwszy Bok : ")
    b = input("Drugi Bok : ")
    wynik = float(a)*float(b)
    wynik2 = float(a)*2+float(b)*2
    print("Pole wynosi : ",wynik," Obwód wynosi : ",wynik2)


def kolo():
    print('    Wybrałes Koło    ')
    a = input("Promień : ")
    wynik = float(a)* float(3.141592)**2
    wynik2 = float(a)* float(3.141592)*2
    print("Pole wynosi : ",wynik," Obwód wynosi : ",wynik2)

def trojkat():
    print('    Wybrałeś Trójkąt   ')
    print("x - Trójkąt( Znamy Długość Boków )")
    print("y - Trójkąt( Znamy Długość Podstawy i Wysokość )")
    ab = input("Wybierz [x/y] : ")
    if ab == "x" :
        a = input("Pierwszy Bok : ")
        b = input("Drugi Bok : ")
        c = input("Trzeci Bok : ")
        a1 = float(a)
        b1 = float(b)
        c1 = float(c)
        wynik = (math.sqrt((a1+b1+c1)*(a1+b1-c1)*(a1-b1+c1)*(-a1+b1+c1)))/4
        wynik3 = a1 + b1 + c1
        print("Pole wynosi: ", wynik," Obwód wynosi : ",wynik3)
    if ab == "y" :
        a = input("Podstawa Trójkąta : ")
        b = input("Wysokość Trójkąta : ")
        a1 = float(a)
        b1 = float(b)
        wynik = a1 * b1/2
        print("Pole wynosi: ", wynik)


def romb():
    print('    Wybrałeś Romb   ')
    a = input(" Długość Przekątnej E : ")
    b = input(" Długość Przekątnej F : ")
    c = input(" Długość Boku : ")
    wynik = float(a)*float(b)
    wynik2 = wynik/2
    wynik3 = float(c)*4
    print("Pole wynosi : ", wynik2, "Obwód wynosi : ", wynik3)

def trapez():
    print('    Wybrałeś Trapez    ')
    a = input("Podstawa Dolna  : ")
    b = input("Podstawa Górna : ")
    c = input("Wysokość Opuszczona Na Podstawę : ")
    d = input("Pierwsze Ramię : ")
    e = input("Drugie Ramię : ")
    wynik = ((float(a)+float(b))*float(c))/2
    wynik2 = float(a)+float(b)+float(d)+float(e)
    print("Pole wynosi : ",wynik," Obwód wynosi : ",wynik2)

def deltoid():
    print('    Wybrałeś Deltoid   ')
    a = input(" Długość Przekątnej E : ")
    b = input(" Długość Przekątnej F : ")
    c = input(" Pierwszy Bok : ")
    d = input(" Drugi Bok : " )
    wynik = (float(a)*float(b))/2
    wynik3 = float(c)*2 + float(d)*2
    print("Pole wynosi : ", wynik,"Obwód wynosi: ", wynik3)

def menuTrojkat():
    print("a - Trójkąt( Znamy Długość Boków )")
    print("b - Trójkąt( Znamy Długość Podstawy i Wysokość )")


while cont:
    menu()
    operacja = input("Co wybierzesz ? ")
    if operacja == "1" : kwadrat()
    elif operacja == "2" : prostokat()
    elif operacja == "3" : kolo()
    elif operacja == "4" : trojkat()
    elif operacja == "5" : romb()
    elif operacja == "6" : trapez()
    elif operacja == "7" : deltoid()
    else: print("Wybrałeś nieprawidlową cyfrę lub literę!")

    operacja2 = input("Kontynuować program? [tak/nie] ")
    if operacja2 == "nie": cont = False
    elif operacja2 == "tak": cont = True
    else: print("Wybrałeś nieprawidlową cyfrę lub literę!")

    #import math
#a = input("Wybierz liczbę : ")
#a2 = input("procent z liczby : ")
#b = float(a)
#b2 = float(a2)
#wynik = float(b) / float(b2)
#print("Procent z tej liczby to : ",wynik,")