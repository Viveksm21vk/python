# Base Class
class Vehicle:
    def start(self):
        print("The vehicle is starting.")

# Subclass 1
class Car(Vehicle):
    def honk(self):
        print("The car is honking. Beep beep!")

# Subclass 2
class Electric:
    def charge(self):
        print("The vehicle is charging.")

# Subclass 3 inheriting from Car and Electric (Hybrid Inheritance)
class ElectricCar(Car, Electric):
    def drive(self):
        print("The electric car is driving silently.")

# Creating Instance
electric_car = ElectricCar()
electric_car.start()    # Output: The vehicle is starting.
electric_car.honk()     # Output: The car is honking. Beep beep!
electric_car.charge()   # Output: The vehicle is charging.
electric_car.drive()    # Output: The electric car is driving silently.