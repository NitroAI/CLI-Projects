import math
print("All maths problem Solaving functions")

def factorial(a):
    x = math.factorial(a)
    print("Factorial of",a,"is: ",x)

def calculator(a,c,b):
    if c=="+":
        print("Ans: ",a+b)
    elif c=="-":
        print("Ans: ",a-b)
    elif c=="*":
        print("Ans: ",a*b)
    elif c=="/":
        print("Ans: ",a/b)
    elif c=="**":
        print("Ans: ",a**b)
    else:
        print(">>Wrong Input Boss!!")

def circle_area(r):
    c = 3.14*r*r
    print("Area is: ",c)

def velocity(d,t):
    c = d/t
    print(c)

def dimenstion(a):
    if a=="area":
        print("Dimenstion of Area: ","[L2]")