person1 = input("wie alt bist du?")
person2 = input("wie jung bist du?")

print(f"Person1 ist: {type(person1)}")
print(f"Person2 ist: {type(person2)}")

person1_int = int(person1)
person2_int = int(person2)
print(f"Person1 ist: {type(person1_int)}")
print(f"Person2 ist: {type(person2_int)}")

addition_person1_person2 = person1 + person2
addition_person1_int_person2_int = person1_int + person2_int
print (f"Die Summe der Jahre /str/ ist: {addition_person1_person2}")
print (f"Die Summe der Jahre /int/ ist: {addition_person1_int_person2_int}")

