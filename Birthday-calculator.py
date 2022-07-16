import datetime

today = datetime.date.today()
birth = datetime.date(2022,9,24)
x = birth - today
print(f"{x.days} days")