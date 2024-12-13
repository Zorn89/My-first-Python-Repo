# Aufgabe 1

a = input ("Value a :") 
b = input ("Value b :")

a_int = int(a)
b_int = int(b)

if a_int > b_int and a_int != b_int:     
    print("Value a is bigger than Value b")

elif a_int == b_int:
    print("Value a same as Value b")

else:
    print("Value b is bigger value a")


# Aufgabe 3

jahr = input("Jahr:")

jahr_int= int(jahr)

if jahr_int >= 1928 and jahr_int <= 1945:
    print("Generation Silent")
elif jahr_int >= 1946 and jahr_int <= 1964:
    print("Generation Boomer")
elif jahr_int >= 1945 and jahr_int <= 1980:
    print("Generation X")
elif jahr_int >= 1981 and jahr_int <= 1996:
    print("Generation Y")
elif jahr_int >= 1997 and jahr_int <= 2010:
    print("Generation Z")
elif jahr_int >= 2011 and jahr_int <= 2025:
    print("Generation Alpha")
else:
    print("Error!")


## anderes Bsp

t=input("Temperatur")
w=input("Wetter ()regen / sonne)")
t_int = int(t) 

if t > 0 and t< 10 and w !="regen":
    print("Trage eine Jacke")
elif w == "regen":
    print("Nimm ein Schirm mit")
elif t>= 11 and t<20 and w != "regen" and w != "windig":
    print("sommerlich kleiden")