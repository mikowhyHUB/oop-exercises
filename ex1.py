# Create a Python class Person with attributes: name and age of type string.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
# Create a display() method that displays the name and age of an object created via the Person class.

    def display(self):
        print("Name is:", self.name)
        print('Age is:', self.age)
# Create a child class Student  which inherits from the Person class and which also has a section attribute.


class Student(Person):
    def __init__(self, name, age, attribute):
        self.attribute = attribute
        super().__init__(name, age)
# Create a method displayStudent() that displays the name, age and section of an object created via the Student class.

    def display_student(self):
        print("Student name is:", self.name)
        print('Student age is:', self.age)
        print('Student attribute:', self.attribute)

# Create a student object via an instantiation on the Student class and then test the displayStudent method.


student1 = Student('Miko', 32, 'dev')
student1.display_student()
