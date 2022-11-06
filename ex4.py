'''
A class regarding an imaginary jet inventory is already defined for you. Also an instant of this Jet class is created and assigned to variable first_item.'''

class Airplane:
    def __init__(self, model, country):
        self.model = model
        self.country = country

jet = Airplane('F16', 'USA')

print(jet.model)