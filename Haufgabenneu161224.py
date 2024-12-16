# Aufgabe 3 

def add(x, y):
    return x + y
def subtract(x,y):
    return x - y
def multi(x,y):
    return x * y
def div(x,y):
    return x / y


# def calculator (add, substrakt, mult, div): 

user_input = input("Wähle eine Grundrechenart (add, substrakt, mult, div): ")
result = (user_input)


user_input_1 = float(input("Gib mir eine Zahl: "))
result = (user_input_1)


user_input_2 = float(input("Gib mir weitere eine Zahl: "))
result = float(user_input_2)

user_input_1 = int(user_input_1)
user_input_2 = int(user_input_2)


if user_input == "add":
    print(f"Ergebnis: {user_input_1 + user_input_2}")
elif user_input == "substrakt":
    print(f"Ergebnis: {user_input_1 - user_input_2}")
elif user_input == "mult":
    print(f"Ergebnis: {user_input_1 * user_input_2}")
elif user_input == "div":
    print(f"Ergebnis: {user_input_1 / user_input_2}")


