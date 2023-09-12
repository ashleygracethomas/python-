a=int(input("enter the value of side"))
b=int(input("enter the value side"))
c=int(input("enter the  value"))
if (a*a+b*b)==(c*c):
    print("right angled triangle")
elif(b*b+c*c==a*a):
    print("right")
elif(a*a+c*c==b*b):
    print("right)
else:
    print("not a right angled triangle")
