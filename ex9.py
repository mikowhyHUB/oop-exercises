'''Write a Python program to create an instance of a specified class and display the namespace of the said instance.'''

class Student:
    def __init__(self,id, name, class_name):
        self.id = id
        self.name = name
        self.class_name = class_name
student = Student('V2', 'Richard', 'V')
print(student.__dict__)
    