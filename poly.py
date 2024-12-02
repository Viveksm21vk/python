class Robot:
    def talk(self):
        print("Robot talks with others.")
    def walk(self):
        print("Robot capable of walking.")
    def charge(self):
        print("Robot charged succesfully.")

class FighterRobot(Robot):
    def talk(self):
        print("Fighter Robot talk.")
    def walk(self):
        print("Fighter Robot walks.")
    def charge(self):
        print("Fighter Robot charged succesfully.")

class TeacherRobot(Robot):
    def talk(self):
        print("Teacher Robot talk.")
    def walk(self):
        print("Teacher Robot walks.")
    def charge(self):
        print("Teacher Robot charged succesfully.")

class DriverRobot(Robot):
    def talk(self):
        print("Driver Robot talk.")
    def walk(self):
        print("Driver Robot walks.")
    def charge(self):
        print("Driver Robot charged succesfully.")

f1 = FighterRobot()
f1.talk()
f1.walk()
f1.charge()

f2 = TeacherRobot()
f2.talk()
f2.walk()
f2.charge()

f3 = DriverRobot()
f3.talk()
f3.walk()
f3.charge()