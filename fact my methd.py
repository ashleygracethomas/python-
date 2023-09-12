
a = int(input("Enter a number: "))
factorial = 1
i = 1

while i <= a:
    factorial = factorial * (a - (i - 1))
    i += 1

print("Factorial:", factorial)
