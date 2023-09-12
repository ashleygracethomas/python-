a=int(input("enter a number"))
sum=0
while a>0:
    rem=a%10
    if rem%2==0:
        sum=sum+rem
    a = a // 10
print(sum)

