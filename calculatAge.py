from datetime import date

def calculatAge(birthDate):
    year = 365.2425
    age = int((date.today() - birthDate).days / year)

    return age
year  = int(input("Enter your birth year: "))
month = int(input("Enter your birth month: "))
day   = int(input("Enter your birth day: "))

print(f"you have {calculatAge(date(year, month, day))} years")
