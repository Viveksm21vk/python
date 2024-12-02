#Single inheritence
#Base Class
class Vehicle:
    def start(self):
        print("The vehicle is starting.")

#Subclass
class Car(Vehicle):
    def start(self):
        print("the Car is starting.")
    def honk(self):
        print("The car is honking. Beep beep!")

v = Vehicle()
v.start()

c = Car()
c.start()
c.honk()