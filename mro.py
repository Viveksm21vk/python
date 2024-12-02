class A:
    def __init__(self):
        print("A is initialized")

class B(A):
    def __init__(self):
        super().__init__()
        print("B is initialized")

class C(A):
    def __init__(self):
        super().__init__()
        print("C is initialized")

class D(C, B):
    def __init__(self):
        super().__init__()
        print("D is initialized")

# Creating an instance
d = D()