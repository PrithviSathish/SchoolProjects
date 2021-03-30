# Program to find the reminder of 2 numbers

n1 = int(input("Enter a number: "))
n2 = int(input("Enter another number: "))

reminder = n1 - ((n1 // n2) * n2)
print("Reminder: ", reminder)


