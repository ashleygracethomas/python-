a=int(input("enter the value"))
b=int(input("enter the value"))
c=int(input("enter the value"))
if a>b and a>c:
    print(a," is greater")
elif b>a and b>c:
    print(b," is greater")
elif (c>a and c>b):
    print(c," is greater")
else:
    print("invalid")