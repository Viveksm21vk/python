class Mentor:
    def define_states(self):
        self.name = "Deep"
        self.tech = "Java"
        self.salary = 25000
    def teach(self):
        print(self.name,"teaches", self.tech ,"for students.")
    def grooming(self):
        print(self.name, "grooming students for interview.")
mentor1 = Mentor()
mentor1.define_states()
mentor1.teach()
mentor1.grooming()
print(mentor1.name)
print(mentor1.tech)
print(mentor1.salary)