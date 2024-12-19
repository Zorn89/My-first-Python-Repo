# Ferien

from datetime import datetime

holidays = dict(
    Weihnachten_2024=(datetime(2024,12,24), datetime(2025,1,2)),
    Ostern_2025=(datetime(2025,4,18), datetime(2024,4,21)),
    Sommerferien_2025=(datetime(2025,8,11), datetime(2025,8,19)),
    Weihnachten_2025=(datetime(2025,12,24), datetime (2026,1,2))
)

input_date_str= input("Gib ein Datum ein(YYYY.MM.DD):") 
input_date= datetime.strptime(input_date_str, "%Y.%m.%d")

holiday_found = False 
for holiday, (start, end) in holidays.items():
    if start <= input_date <= end:
        print(f"{input_date_str} is {holiday} in vacation")
        holiday_found = True
        break

if not holiday_found: 
    print(f"{input_date_str} is in business!")

    diff = year.replace(year=today.year + 1) - today
    return diff.days