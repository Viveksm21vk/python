def calculate(a,b):
    print("About to start calculation....")
    try:
        div = a/b
        print("Division =",div)
        c = 10
        add = a + c
        print("Addition = ", add)
    except ZeroDivisionError:
        print("Division by zero is not possible......")
    except NameError:
        print("Variable not found.....")
print("Program is starting......")
n1 = int(input("Enter 1st number - "))
n2 = int(input("Enter 2nd number - "))
calculate(n1, n2)
print("Program is ended.....")