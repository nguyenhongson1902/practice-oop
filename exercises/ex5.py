"""OOP Exercise 5: Define property that should have the same value for every class instance"""


class Vehicle:
    color = 'White'
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

class Bus(Vehicle):
    pass

class Car(Vehicle):
    pass

bus1 = Bus('School bus', 200, 10)
print(bus1.color)

car1 = Car('My car', 300, 20)
print(car1.color)