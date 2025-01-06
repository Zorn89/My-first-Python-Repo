# Abfrage  mit Loop


for _ in range(3): 
    print("Hallo") #Wiederholung 3 mal Hallo wegen for _ 

counter = 0 
while counter < 3:
        print("Hallo von while")
        counter = counter +1 


gerichte =[]

for _ in range(3): 
      user_input = ("Gib mir ein Lieblingsgericht")
      gerichte.append(user_input) 
      print(f"Meine Liste: {gerichte}") 

# gerichte: ["pizza","nudeln","reis"]


for ge in gerichte: 
      print(f"Meine Lieblingsgerichte: {ge}")