class Person:
    def __init__(self):
        self.id = 22
class Developer(Person):
    def __init__(self,id,name,salary):
        self.id = id
        self.name = name
        self.salary = salary
        super().__init__()
        print(self.id)
    def display_info(self):
        print(f"ID: {self.id}, Name: {self.name}, Salary: {self.salary}")
d = Developer(1,"Vivek",20000)
d.display_info()