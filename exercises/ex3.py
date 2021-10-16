"""OOP Exercise 3: Create a child class Bus that will inherit all of the variables and methods of the Vehicle class"""


class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage


class Bus(Vehicle):
    def __init__(self, name, max_speed, mileage):
        super().__init__(name, max_speed, mileage)

    def display(self):
        print('Name:', self.name)
        print('Max speed:', self.max_speed)
        print('Mileage:', self.mileage)


bus1 = Bus('Yen Vien', 200, 10)
bus1.display()
