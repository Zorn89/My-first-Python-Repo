## Taxometer

start_price = 4,50 
km = int(input("Bitte KM eingeben:"))
if km > 2:
    costs = 2.5
else: 
    costs = 2.7
total_expenses = start_price + costs * km
print("Die Kosten:", total_expenses)