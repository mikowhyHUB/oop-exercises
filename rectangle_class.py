class Rectangle:
    def __init__(self, lenght, width):
        self.length = lenght
        self.width = width

    def perimeter(self):
        return 2*(self.length + self.width)

    def area(self):
        return self.length * self.width

    def display(self):
        print('Lenght is:', self.length)
        print('Width is:', self.width)
        print('Perimeter is:', self.perimeter())
        print('Area is:', self.area())


class Parallelepipede(Rectangle):
    def __init__(self, lenght, width, height):
        Rectangle.__init__(self, lenght, width)
        self.height = height

    def volume(self):
