class Robot:
    def talk(self):
        print("Robot talks with others.")
    def walk(self):
        print("Robot capable of walking.")
    def charge(self):
        print("Robot charged succesfully.")
class FighterRobot(Robot):
    def fight(self):
        print("Robo can fight.")
class TeacherRobot(Robot):
    def teach(self):
        print("Robo can teach.")
class DriverRobot(Robot):
    def drive(self):
        print("Robo can drive.")

def access_robo(robo):
    robo.talk()
    robo.walk()
    robo.charge()
    if type(robo) == FighterRobot:
        FighterRobot().fight()
    if type(robo) == TeacherRobot:
        TeacherRobot().teach()
    if type(robo) == DriverRobot:
        DriverRobot().drive()

f1 = FighterRobot()
access_robo(f1)
f2 = TeacherRobot()
access_robo(f2)

f3 = DriverRobot()
access_robo(f3)