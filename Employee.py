class Employee:
    # Class attributes
    ecompany = "KodNest Pvt Ltd"
    def __init__(self,eid, ename,esalary):
        self.eid = eid
        self.ename = ename
        self.esalary = esalary
    def do_job(self):
        print(f"{self.ename} working in {Employee.ecompany}")
    def intro(self):
        print(f"{self.ename} with ID: {self.eid} working in the {Employee.ecompany} with salary of {self.esalary}.")
    @staticmethod
    def goto_team_outing():
        print("Go to team outing.")
    @classmethod
    def change_company_name(cls):
        Employee.ecompany = "KodNest"
id1 = int(input("Entre ID of first employee: "))
name1 = input("Enter name of first employee: ")
salary1 = float(input("Enter salary of first Employee: "))
e1 = Employee(id1,name1,salary1)
e1.do_job()
e1.intro()
Employee.goto_team_outing()
Employee.change_company_name()
id2 = int(input("Entre ID of second employee: "))
name2 = input("Enter name of second employee: ")
salary2 = float(input("Enter salary of second Employee: "))
e2 = Employee(id2,name2,salary2)
e2.do_job()
e2.intro()
Employee.goto_team_outing()
id3 = int(input("Entre ID of third employee: "))
name3 = input("Enter name of third employee: ")
salary3 = float(input("Enter salary of third Employee: "))
e3 = Employee(id3,name3,salary3)
e3.do_job()
e3.intro()
Employee.goto_team_outing()