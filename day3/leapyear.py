year = int(input("Enter year to check: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 4 == 0 and year % 100 == 0 and year % 400 == 0):
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")
