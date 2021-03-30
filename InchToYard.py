# Convert inches to yard (12inches = 1ft and 3ft=1 yard)

inch = float(input("Enter the number of inches: "))

print("The number is: ", inch // 36, "Yards,", (inch % 36) // 12, "feet,", inch % 12, "Inches")


