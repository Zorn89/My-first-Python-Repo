

def add(x, y):
    return x + y
def sub(x,y):
    return x - y
def multi(x,y):
    return x * y
def div(x,y):
    return x / y

def calculator ():
    op = input("Operation (+,-,*,/):")

    zahl1 = float(input("Erste Zahl:"))
    zahl2 = float(input("Zweite Zahl:"))

    if op == "+": 
        print(f"{zahl1} + {zahl2} = {add(zahl1, zahl2)}") 

    elif op == "-":
         print(f"{zahl1} -{ zahl2} = {sub(zahl1, zahl2)}") 

    elif op == "*":
         print(f"{zahl1} *{ zahl2} = {multi(zahl1, zahl2)}") 

    elif op == "-/":
         print(f"{zahl1} /{ zahl2} = {div(zahl1, zahl2)}") 
    else:
        print("Bitte gültige Opertation auswhählen")
        
        
    calculator ():

