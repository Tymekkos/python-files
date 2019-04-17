print()
def menu():
    print("1 - kwadrat")
    print("2 - prostokąt")
    print("3 - koło")

def kwadrat():
    print('    Wybrałes Kwadrat    ')
    a = input(" Długość Boku : ")
    b = float(a)
    wynik = float(b)*float(b)
    wynik2 = float(b)*4


def prostokąt():
    print('    Wybrałes Prostokąt    ')
    a = input("Pierwszy Bok : ")
    b = input("Drugi Bok : ")
    wynik = float(a)*float(b)
    return wynik

def koło():
    print('    Wybrałes Koło    ')
    a = input("Promień : ")
    wynik = float(a)* float(3.141592)**2
    return wynik

    print(menu())
    operacja = input("Co wybierzesz ? ")
    while operacja == 1 or 2 or 3 :
       if operacja=="1": print("Pole to : ",wynik," Obwód to : ",wynik2)
       elif operacja=="2": print("Pole to : \n",prostokąt())
       elif operacja=="3": print("Pole to : \n",koło())