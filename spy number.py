a=int(input("enter a number"))
sum=0
mul=1
while(a):
    digit=a%10
    print("digits",digit)
    sum = sum + digit
    print("sum", sum)
    mul= mul* digit
    print("mul",mul)
    a = a // 10
if mul==sum:
    print("the number is a spy number")
else:
    print("the number is not a spy number")