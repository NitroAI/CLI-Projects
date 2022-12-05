import calpy
from calpy import circle_area,velocity,factorial,calculator

while True: 
    print('''
    Sellect The Number What You Want to Do!

       | 1.Factorial
       | 2.Area of Circle
       | 3.Velocity
       | 4.Calculator
    ''')
    option = int(input("Sellect Number: "))
    if option == 1:
        n = int(input("Number Here: "))
        factorial(n)
        print("____________________________________________________________________________________________________")
    elif option == 2:
        n = int(input("Enter Radious Here: "))
        circle_area(n)
        print("____________________________________________________________________________________________________")
    elif option == "":
        pass
    elif option == 4:
        n1 = int(input("Enter First Number: "))
        n2 = input("Enter Symbol(+,-,*,/,**): ")
        n3 = int(input("Enter Second Number: "))
        calculator(n1,n2,n3)
        print("____________________________________________________________________________________________________")
    elif option == "":
        pass
    elif option == "":
        pass
    elif option == "":
        pass
    elif option == "":
        pass
    elif option == "":
        pass
    else:
        print(">>Wrong Option")
        print("____________________________________________________________________________________________________")
