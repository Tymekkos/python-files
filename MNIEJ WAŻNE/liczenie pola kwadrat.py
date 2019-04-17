print('Ten program umożliwi Ci obliczenie pola kwadratu i prostokąta')
print('Wybierz liczbę 1 lub 2 
a = input('Bok kwadratu: ')
b = float(a)
print(b*b)





def kwadrat():
    a = input("Pierwsza liczba ")
    b = float(a)
    wynik = float(b)*float(b)
    return wynik
 
def prostokąt():
    a = input("Pierwszy Bok ")
    b = input("Drugi Bok ")
    wynik = float(a)*float(b)
    return wynik
