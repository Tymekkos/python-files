print('Ta aplikacja pozwala Ci obliczyc pole wybranej figury')
print('Czytaj uwaznie wszystkie instrukcje!')
print('Wybierz figurę, wpisując cyfre danej figury')
odp = ''
odp = input('1. Prostokąt 2. Kwadrat 3. Koło 4. Romb')
while True:
   if odp=="1":
       dlugosc = input('Podaj dlugosc dluzszego boku prostokata: ')
       szerokosc = input('Podaj dlugosc krotszego boku prostokata: ')
       szerokosc = int(szerokosc)
       dlugosc = int(dlugosc)
       pole = (dlugosc * szerokosc)
       print ('Pole wynosi: ', pole)
       odp = str.lower(input('Jezeli chcesz wybrac inna figure napisz "tak". Jezeli nie napisz "nie" :)'))
   if odp=="tak":
       odp = input('1. Prostokąt 2. Kwadrat 3. Koło 4. Romb')
   if odp =="nie":
       print('Koniec programu!')
       break
   elif odp=='':
       print('Koncze program, bo nie wybrales figury!')
       break
   if odp=="2":
       bok = input('Podaj dlugosc boku kwadratu: ')
       bok = int(bok)
       pole = (bok*bok)
       print('Pole wynosi:', pole)
       odp = str.lower(input('Jezeli chcesz wybrac inna figure napisz "tak". Jezeli nie napisz "nie" :)'))
   if odp=="tak":
       odp = input('1. Prostokąt 2. Kwadrat 3. Koło 4. Romb')
   if odp =="nie":
       print('Koniec programu!')
       break
   elif odp=='':
       print('Koncze program, bo nie wybrales figury!')
       break
