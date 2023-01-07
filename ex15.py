'''
Write a Python program to create a Vehicle class with max_speed and mileage instance attributes.
'''


class Vehicle:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage


volvo = Vehicle(30, 300)
bmw = Vehicle(40, 400)
print(bmw.mileage, volvo.max_speed)
