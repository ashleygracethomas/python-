a=int(input("enter a number"))
b=int(input("enter a number"))
while a>0:
    rem=a%10
    a=a//10
if  rem==b:
    print("yes")
else:
    print("no")



