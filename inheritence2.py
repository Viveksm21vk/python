class Parent:
    def __init__(self):
        print("Parent class constructor.")

class Child1(Parent):
    pass

class Child2(Parent):
    def __init__(self):
        print("Child2 class constructor.")

c1 = Child1()
c2 = Child2()