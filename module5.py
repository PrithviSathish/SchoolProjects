year = int(input("Enter a year: "))
if len(str(year)) != 4:
    print("Please enter a valid year!")
else:
    if year % 100 == 0 and year % 400 == 0:
        print("The year is a leap year")
    elif year % 100 != 0 and year % 4 == 0:
        print("The year is a leap year")
    else:
        print("The year is not a leap year")
