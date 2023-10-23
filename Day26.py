def is_leap_year(year):
    return (year // 4) * 4 == year and (year // 100) * 100 != year or (year // 400) * 400 == year

year = int(input("Enter a year: "))

if is_leap_year(year):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")
