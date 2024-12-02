class Student:
    def define_states(self):
        self.kod_id = 101
        self.name = "Vivek S M"
        self.branch = "ECE"
        self.yop = 2024
    def study(self):
        print("Student study.")
    def give_interviews(self):
        print("Student give interviews.")
student1 = Student()
student1.define_states()
print("Student Name:",student1.name)
print("Student ID:",student1.kod_id)
print("Student Branch:",student1.branch)
print("Year of Passout:",student1.yop)
student1.study()
student1.give_interviews()