class Student:
    def __init__(self,roll,name):
        self._roll = roll
        self.name = name
    
    def get_roll(self):
        return self._roll
    
    def get_name(self):
        return self.name
    
    def set_roll(self,roll):
        if(roll > 0):
            self._roll = roll
        else:
            print("Please enter valid roll number")
    def set_name(self,name):
        self.name = name
st = Student(101,"Vivek")
print(st.get_name())
print(st.get_roll())

st.set_name("Vivek S M")
st.set_roll(-1)
st.set_roll(102)

print(st.get_name())
print(st.get_roll())

#print(st.roll)
print(st.name)
