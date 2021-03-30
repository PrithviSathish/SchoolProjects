# Find the type of triangle

s1 = int(input("Enter the length of side 1: "))
s2 = int(input("Enter the length of side 2: "))
s3 = int(input("Enter the length of side 3: "))

if s1 == s2 == s3:
    print("The triangle is Equilateral")
elif (s1 == s2) or (s2 == s3) or (s3 == s1):
    print("The triangle is isoscles")
else:
    print("The triange is scalene")


