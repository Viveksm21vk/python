def calculate(a,b):
    try:
        div = a/b
    except:
        print("Division by zero is not possible......")
    else:
        print("Division =",div)
n1 = int(input("Enter 1st number - "))
n2 = int(input("Enter 2nd number - "))
calculate(n1, n2)
