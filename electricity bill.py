unit=int(input("enter the units that you havr consumed"))
if unit<=100:
 totalamountconsumed=unit*1.5
 fixedcharge=25
elif unit<=200:
 totalamountconsumed=(100*1.5)+((unit-100)*2.5)
 fixedcharge=50
elif unit<=300:
 totalamountconsumed=(100*1.5)+((200-100)*2.5)+(units-300)*4
 fixedcharge=75
elif unit<=350:
 totalamountconsumed=(100*1.5)+(200-100)*2.5+(300-200)*4+(units-350)*5
 fixedcharge=100
else:
 totalamountconsumed=0
 fixedcharge=1500
total= totalamountconsumed+fixedcharge
print("electricity bill is:",total)
