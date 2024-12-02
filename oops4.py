class Student():
    def __init__(self1,kod_id,name,branch,yop):
        self1.kod_id = kod_id
        self1.name = name
        self1.branch = branch
        self1.yop = yop
    def graduate(self1):
        print(self1.name,"graduate in branch",self1.branch,"in the year",self1.yop)
    def give_interview(self1):
        print(self1.name,"give interview.")
student1 = Student(101,"Vivek S M","ECE",2024)
print("ID:",student1.kod_id)
print("Name:",student1.name)
print("Branch:",student1.branch)
print("YOP:",student1.yop)
student1.graduate()
student1.give_interview()