class Mentor:

    def __init__(self,name,tech):
        self.name = name
        self.tech = tech
    
    def teach(self):
        print("Mentor teaches students.")
    
    def grooming(self):
        print("Mentor grooming students.")
name = input("Enter Mentor name: ")
tech = input("Enter Tchnology: ")
m = Mentor(name,tech)
print(m.name)
print(m.tech)
m.teach()
m.grooming()