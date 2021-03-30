n = int(input("Enter a number: "))

prime = True
for i in range(2, n):
    if n % i == 0:
        prime = False
        break


if prime == False:
    print("The number is not a prime number")
else:
    print("The number is a prime number")