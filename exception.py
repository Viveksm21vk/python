def div(a, b):
    try:
        res = a/b
        print("Result =", res)
    except ZeroDivisionError:
        print("Division by zero is not possible...")
a = int(input("Please ente numerator: "))
b = int(input("Please enter denomenator: "))
div(a,b)