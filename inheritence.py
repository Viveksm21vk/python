class SoftwareEngineer:
    def __init__(self,eid,ename,esalary,company):
        self.eid = eid
        self.ename = ename
        self.esalary = esalary
        self.company = company
    
    def intro(self):
        print(f"ID: {self.eid}, Name: {self.ename}, Salary: {self.esalary}, Company: {self.company}")
    
    def software_skills(self):
        print("He has software skills.")

class Person:
    def walking(self):
        print("He is walking.")
    def speek(self):
        print("He is speeking.")
class Developer(SoftwareEngineer,Person):
    def coding(self):
        print("Developer has coding skills.")
class Tester(SoftwareEngineer,Person):
    def debugging(self):
        print("Tester has debugging skills.")
dev1 = Developer(101,"Vivek S M",300000,"KodNest")
dev1.intro()
dev1.software_skills()
dev1.coding()
dev1.walking()
dev1.speek()

test1 = Tester(102,"Karthik B S",300000,"KodNest")
test1.intro()
test1.software_skills()
test1.debugging()
test1.walking()
test1.speek()