class Parent:
    def fun(self):
        print("Parent fun")

class Child(Parent):
    def fun(self):
        print("Child fun")
        super().fun()
c = Child()
c.fun()