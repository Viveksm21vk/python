class Student:
    def __init__(self):
        self.__roll = 101
        self._cgpa = 8.0
        self.name = "deep"
st = Student()
#print(st.__roll)
print(st._Student__roll)
print(st._cgpa)
print(st.name)       