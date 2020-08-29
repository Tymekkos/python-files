import time
print("Program do obliczania masy czasteczkowej substancji:")
print("-Wpisz cały wzór lub tylko pierwiastek(pamiętaj o poprawnym zapisie)")
symbols ={
"H" : 1,
"He" : 4,
"Li" : 7,
"Be" : 9,
"B" : 11,
"C" : 12,
"N" : 14,
"O" : 16,
"F" : 19,
"Ne" : 20,
"Na" : 23,
"Mg" : 24,
"Al" : 27,
"Si" : 28,
"P" : 31,
"S" : 32,
"Cl" : 35,
"Ar" : 40,
"K" : 39,
"Ca" : 40,
"Sc" : 45,
"Ti" : 48,
"V" : 51,
"Cr" : 52,
"Mn" : 55,
"Fe" : 56,
"Co" : 59,
"Ni" : 59,
"Cu" : 64,
"Zn" : 65,
"Ga" : 70,
"Ge" : 73,
"As" : 75,
"Se" : 79,
"Br" : 80,
"Kr" : 84,
"Rb" : 85,
"Sr" : 88,
"Y" : 89,
"Zr" : 91,
"Nb" : 93,
"Mo" : 96,
"Tc" : 99,
"Ru" : 101,
"Rh" : 103,
"Pd" : 106,
"Ag" : 108,
"Cd" : 112,
"In" : 115,
"Sn" : 119,
"Sb" : 122,
"Te" : 128,
"I" : 127,
"Xe" : 131,
"Cs" : 133,
"Ba" : 137,
"La" : 139,
"Ce" : 140,
"Pr" : 141,
"Nd" : 144,
"Pm" : 147,
"Sm" : 150,
"Eu" : 152,
"Gd" : 157,
"Tb" : 159,
"Dy" : 163,
"Ho" : 165,
"Er" : 167,
"Tm" : 169,
"Yb" : 173,
"Lu" : 175,
"Hf" : 178,
"Ta" : 181,
"W" : 184,
"Re" : 186,
"Os" : 190,
"Ir" : 192,
"Pt" : 195,
"Au" : 197,
"Hg" : 201,
"Tl" : 204,
"Pb" : 207,
"Bi" : 209,
"Po" : 209,
"At" : 210,
"Rn" : 222,
"Fr" : 223,
"Ra" : 226,
"Ac" : 227,
"Th" : 232,
"Pa" : 231,
"U" : 238,
"Np" : 237,
"Pu" : 244,
"Am" : 243,
"Cm" : 247,
"Bk" : 247,
"Cf" : 251,
"Es" : 252,
"Fm" : 257,
"Md" : 258,
"No" : 259,
"Lr" : 260
}
dalej = True 

while dalej:
  next_mark = ""
  mass = 0
  wzor = input("")
  for symbol in wzor:
    if next_mark == "":
      next_mark = symbol
      continue
    if symbol.isdigit():
      mass += symbols[next_mark]*int(symbol)
      next_mark = ""
    elif symbol.isupper():
      mass += symbols[next_mark]
      next_mark = symbol
    elif symbol.islower():
      next_mark+= symbol

  if next_mark !="":
     mass += symbols[next_mark]

  time.sleep(1)
  print("masa substancji wynosi", mass,"u")
  
  repeat = input("Kontynuować program? [tak/nie] ")
  if repeat == "nie":
      print("")
      print("Dziękuję Ci za korzystanie z mojego programu,")
      print("Tymek :)")
      time.sleep(1.8)
      dalej = False
  elif repeat == "tak":
      dalej = True
      print("")
      print("-Wpisz cały wzór lub tylko pierwiastek(pamiętaj o poprawnym zapisie)")


