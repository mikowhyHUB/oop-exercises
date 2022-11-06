'''First make your function so that it takes to parameters: x and y. x will be the number being raised and y will be the power. So, users can raise numbers to any power! Also let's change the function's name to power.

Also let's add a string representation quickly, so that when a user prints the class they get a meaningful description.
'''

class Myfunc:
    def power(x, y):
        return x ** y
    def __str__(self):
        return "some math stuff"

ans = Myfunc.power(3,2)
ans1 = Myfunc.power(5,6)
print(Myfunc())
print(ans)
print(ans1)