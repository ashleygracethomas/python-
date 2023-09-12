num=int(input("enter a number"))
sum=0
while num>0:
     digitseperate=num%10
     sum=sum+digitseperate
     num = num // 10
     print(sum)
     if num==0 and sum>9:
        num=sum
        sum=0





