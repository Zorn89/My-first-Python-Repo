def begruessung(name): # Klammer fehlt (name)
    print("Hallo, " + name) # fehlte der Einschub und name anstatt Name

def addiere_zahlen(a, b): # : fehlte
    ergebnis = a + b
    return ergebnis # ergebis war falsch  

def subtrahiere_zahlen(a, b):
    return a - b # c anstatt b

def main(): # ein : fehlte
    zahl1 = int(input("Gib eine Zahl ein: "))  #Der input()-Befehl gibt standardmäßig einen String zurück. Daher int zum umwandeln 
    zahl2 = int(input("Gib eine weitere Zahl ein: "))  # #Der input()-Befehl gibt standardmäßig einen String zurück. Daher int zum umwandeln 

    summe = addiere_zahlen(zahl1, zahl2)  
    print("Die Summe ist: " + str(summe))  # str hat gefehlt

    differenz = subtrahiere_zahlen(zahl1, zahl2)  
    print("Die Differenz ist: " + str(differenz))  # str hat gefehlt

    begruessung("Max")  

if __name__ == "__main__": # ein = fehlte
    main()
