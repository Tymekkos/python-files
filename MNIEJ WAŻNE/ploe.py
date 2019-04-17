while True:
 
   print('1. Prostokąt\n2. Kwadrat\n3. Koło\n4. Romb\n0. Wyjście z programu')
   odp = input('podaj liczbę:')
 
    try:
       odp = int(odp)
       if odp == 0:
           print("Koniec")
           break
       elif odp == 1:
           prostokat()
           if not tak_nie():
               print('Koniec programu!')
               break;
       elif odp == 2:
           kwadrat()
           if not tak_nie():
               print('Koniec programu!')
               break;
       elif odp == 3:
           koło()
           if not tak_nie():
               print('Koniec programu!')
               break;
       elif odp == 4:
           romb()
           if not tak_nie():
               print('Koniec programu!')
               break;
       else:
           print("Wybrano złą liczbę !!!")
    except:
       print('Wpisano coś innego niż liczba !!!!')
       
