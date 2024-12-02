# Base Class
class Appliance:
    def plug_in(self):
        print("The appliance is plugged in.")

# Subclass 1
class WashingMachine(Appliance):
    def wash_clothes(self):
        print("The washing machine is washing clothes.")

# Subclass 2
class Refrigerator(Appliance):
    def cool_food(self):
        print("The refrigerator is cooling food.")

# Creating Instances
washer = WashingMachine()
fridge = Refrigerator()

washer.plug_in()       # Output: The appliance is plugged in.
washer.wash_clothes()  # Output: The washing machine is washing clothes.

fridge.plug_in()       # Output: The appliance is plugged in.
fridge.cool_food()     # Output: The refrigerator is cooling food.