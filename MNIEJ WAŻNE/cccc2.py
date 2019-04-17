def validate(prompt, parse, errmsg=''):
   while True:
       try:
           return parse(input(prompt))
       except Exception as why:
           if errmsg:
               print(errmsg)
           else:
               print(why)
 
def get_num (prompt=None):
   prompt = prompt if prompt else "podaj liczbę: "
   errmsg = "tylko liczby"
   return validate (prompt, float, errmsg)
 
def get_yes_or_no ():
   def is_yes_or_no (text):
       if text.lower() in ('tak', 'yes'):
           return 'yes'
       elif text.lower() in ('nie', 'no'):
           return 'no'
       else:
           raise ValueError ("Tylko tak lub nie")
   prompt = "Kontynuować program? [tak/nie]: "
   return validate (prompt, is_yes_or_no)
 
def get_fig_nr():
   def parse(nr):
       try:
           nr = int (nr)
           if 1 == nr :
               return nr
           else:
               raise
       except:
           raise ValueError ("Tylko liczba 1")
   prompt = "Wybierz liczbę 1, aby obliczyć pole kwadratu: "
   return validate(prompt, parse)
 
if __name__ == "__main__":
   print('Ta aplikacja pozwala Ci obliczyc pole wybranej figury')
   print('Czytaj uwaznie wszystkie instrukcje!')
   print('Wybierz figurę, wpisując cyfre danej figury')
   while get_yes_or_no() == 'yes':
       print("  1. kwadrat")
 
       fig = get_fig_nr()
       if fig == 1:
           field = get_num ("Podaj długość boku kwadratu: ") ** 2
      
       else:
           pass
 
       print("Pole wynosi:", field)
