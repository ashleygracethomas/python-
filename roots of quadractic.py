a=int(input("enter the value of coeffient of x**2"))
b=int(input("enter the  value of coeefient of x"))
c=int(input("enter the value of constant term"))
d=(b*b)-(4*a*c)
if d>0:
    root1=(-b+((d)**1/2)/(2*a))
    root2=(-b-((d)**1/2)/(2*a))
    print("the two distinct roots are ",root1 ,root2)
elif d==0:
    root1=root2=-b/(2*a)
    print("two eqaul and real roots are ",root1,root2)
elif d<0:
    root1=root2=-b/(2*a)
    imaginary=(-d)**0.5/(2*a)
    print("two distinct complex roots",root1,root2)

