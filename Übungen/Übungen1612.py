# Nachfrage nach Alter und Ausgabe

def altersabfrage():
    user_input = input("Wie alt bist du?")
    result = (user_input)
    print(result)


altersabfrage()



def namensabfrage():
    name = input("Wie heißt du?")
    print  (f"Du heist {name}.")
 

def namensabfrage2(): 
    name = input ("Gib deinen Namen an: ")
    return (f"Du bist {name}.")

print(namensabfrage())
print(namensabfrage2())


namensabfrage()



if user_input == "add":
    print(f"Ergebnis: {user_input_1 + user_input_2}")
elif user_input == "substrakt":
    print(f"Ergebnis: {user_input_1 - user_input_2}")
elif user_input == "mult":
    print(f"Ergebnis: {user_input_1 * user_input_2}")
elif user_input == "div":
    print(f"Ergebnis: {user_input_1 / user_input_2}")