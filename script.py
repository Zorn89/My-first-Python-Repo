first_name = "Jan"
last_name = "Zorn"


zahl1 = 2
zahl2 = 3

note1 = 2
note2 = 4
note3 = 1

print(first_name+" "+last_name)

print("Zahl 1 + Zahl 2:", zahl1 + zahl2) 
print("Zahl 1 * Zahl 2:", zahl1 * zahl2) 
print("Zahl 1 / Zahl 2:", zahl1 / zahl2) 
print("Zahl 2 / Zahl 1:", zahl2 / zahl1) 
print("Zahl 2 - Zahl 1:", zahl2 - zahl1) 

inp_lst = [note1, note2,note3]

sum_lst = sum(inp_lst)

lst_avg = sum_lst / len(inp_lst)
print("Durchschnittswert der Liste:\n") 
print(lst_avg) 
print("Durchschnittswert der Liste auf 3 Dezimalstellen gerundet:\n")
print(round(lst_avg,3))

