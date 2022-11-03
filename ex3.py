# Create a Coputation class with a default constructor (without parameters) allowing to perform various calculations on integers numbers.
class Computation:
    def __init__(self):
        pass
# Create a method called Factorial() which allows to calculate the factorial of an integer. Test the method by instantiating the class.

    def factorial(self, num):
        f = 1
        for i in range(1, num+1):
            f = f * i
        return f
# Create a method called Sum() allowing to calculate the sum of the first n integers 1 + 2 + 3 + .. + n. Test this method.

    def sum(self, num):
        s = 1
        for i in range(1, num+1):
            s += 1
        return s
# Create a method called testPrim() in  the Calculation class to test the primality of a given integer. Test this method.

    def test_prim(self, num):
        p = 0
        for i in range(1, num+1):
            if i % 2 == 0:
                p += i

# Create  a method called testPrims() allowing to test if two numbers are prime between them.
# Create a tableMult() method which creates and displays the multiplication table of a given integer. Then create an allTablesMult() method to display all the integer multiplication tables 1, 2, 3, ..., 9.
# Create a static listDiv() method that gets all the divisors of a given integer on new list called  Ldiv. Create another listDivPrim() method that gets all the prime divisors of a given integer.
