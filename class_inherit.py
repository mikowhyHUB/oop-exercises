from turtle import speed


class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage


class Child(Vehicle):
    pass


car1 = Child('Tom', 320, 4000)

print(car1.name, car1.max_speed, car1.mileage)
