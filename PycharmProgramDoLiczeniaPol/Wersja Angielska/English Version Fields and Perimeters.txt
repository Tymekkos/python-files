
# -*- coding: utf-8 -*-
import math

print("")
print("That's a program for counting fields of geometric figures")
print("Enter 1 to select a square, 2 to select a rectangle, etc.")
cont = True

def menu():
    print("1 - Square")
    print("2 - Rectangle")
    print("3 - Circle")
    print("4 - Triangle")
    print("5 - Rhombus")
    print("6 - Trapeze")
    print("7 - Deltoid")


def square():
    print('    You Choosed Triangle    ')
    a = input(" Side Length : ")
    b = float(a)
    result = float(b)*float(b)
    result2 = float(b)*4
    print("Field is : ",result," Perimeter is : ",result2)



def rectangle():
    print('    You Choosed Rectangle    ')
    a = input("First Side : ")
    b = input("Second Side: ")
    result = float(a)*float(b)
    result2 = float(a)*2+float(b)*2
    print("Field is : ",result," Perimeter is : ",result2)


def circle():
    print('   You Choosed Circle   ')
    a = input("Radius : ")
    result = float(a)* float(3.141592)**2
    result2 = float(a)* float(3.141592)*2
    print("Field is : ",result," Perimeter is : ",result2)

def triangle():
    print('    You Choosed Triangle   ')
    print("x - Triangle( You Know The Length Of The Sides )")
    print("y - Triangle( You Know The Length Of The Base And Height )")
    ab = input("Choose [x/y] : ")
    if ab == "x" :
        a = input("First Side : ")
        b = input("Second Side : ")
        c = input("Third side : ")
        a1 = float(a)
        b1 = float(b)
        c1 = float(c)
        result = (math.sqrt((a1+b1+c1)*(a1+b1-c1)*(a1-b1+c1)*(-a1+b1+c1)))/4
        result3 = a1 + b1 + c1
        print("Field is : ", result," Perimeter is: ",result3)
    if ab == "y" :
        a = input("Base Of Triangle : ")
        b = input("Height Of Triangle : ")
        a1 = float(a)
        b1 = float(b)
        result = a1 * b1/2
        print("Pole wynosi: ", result)


def rhombus():
    print('   You Choosed Rhombus   ')
    a = input(" The Length Of Diagonal E : ")
    b = input(" The Length Of Diagonal F : ")
    c = input(" Side Length : ")
    result = float(a)*float(b)
    result2 = result/2
    result3 = float(c)*4
    print("Field is : ", result2, " Perimeter is : ", result3)
def trapeze():
    print('    You Choosed Trapeze    ')
    a = input("Lower Base  : ")
    b = input("Upper Base: ")
    c = input("Height Lowered On The Base : ")
    d = input("First Arm : ")
    e = input("Second Arm : ")
    result = ((float(a)+float(b))*float(c))/2
    result2 = float(a)+float(b)+float(d)+float(e)
    print("Field is : ", result, " Perimeter is : ", result2)

def deltoid():
    print('    You Choosed Deltoid   ')
    a = input(" The Length Of Diagonal E : ")
    b = input(" The Length Of Diagonal F : ")
    c = input(" First Side : ")
    d = input(" Second Side: " )
    result = (float(a)*float(b))/2
    result2 = float(c)*2 + float(d)*2
    print("Field is : ", result, " Perimeter is : ", result2)

def menuTriangle():
    print("a - Triangle( You Know The Length Of The Side )")
    print("b - Triangle( You Know The Base and Height )")

while cont:
    menu()
    operation = input("What Will You Choose ? ")
    if operation == "1" : square()
    elif operation == "2" : rectangle()
    elif operation == "3" : circle()
    elif operation == "4" : triangle()
    elif operation == "5" : rhombus()
    elif operation == "6" : trapeze()
    elif operation == "7" : deltoid()
    else: print("You choosed wrong number or letter!")

    operation2 = input("Would You like to continue this program? [yes/no] ")
    if operation2 == "no": cont = False
    elif operation2 == "yes": cont = True