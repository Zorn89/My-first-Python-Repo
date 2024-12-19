from datetime import datetime

bday = datetime.date(2005,10,13)

bday = "2003.05.27"

new_bday = datetime.strptime(bday, "%Y.%m.%d")
print(new_bday)