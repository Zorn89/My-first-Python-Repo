# aktuelles Datum

import datetime

x = datetime.datetime.now()

print(x) 

# Tage bis zum Jahresende 


def end_of_year(year):
    today = datetime.date.today()
    diff = year.replace(year=today.year) - today
    if diff.days < 0:
        diff = year.replace(year=today.year + 1) - today
    return diff.days


def main():
    days = end_of_year(datetime.date(2024,12,31))
    print(f"Es sind noch {days} Tage bis Jahresende ")

  

if __name__ == '__main__':
    main()


# Tage bis Datum

user_input = input("Gib ein Datum ein (YYYY.MM.DD): ")
result = (user_input)



def tage(year):
    today = datetime.date.today()
    diff = year.replace(year=today.year) - today
    if diff.days < 0:
        diff = year.replace(year=today.year + 1) - today
    return diff.days


def main():
    days = end_of_year(datetime.date(user_input))
    print(f"Es sind noch {days} Tage bis Jahresende ")

  

if __name__ == '__main__':
    main()







# Wochentag berechnen


def get_weekday():
    weekdays = ('Montag', 'Dienstag', 'Mittwoch',
                'Donnerstag', 'Freitag', 'Samstag', 'Sonntag')
    date = input('Datum (yyyy-mm-dd): ')
    return weekdays[(date).weekday()]

