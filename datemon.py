day=int(input("Enter the day(1-31):"))
month=int(input("Enter the month(1-12):"))
year=int(input("Enter the year:"))
print(f"Entered date: {day}-{month}-{year}")
if(year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"This year is leap year",year)
else:
    print(f"This year is not leap year",year)