'''In this exercise create a class named myfunc and inside it place a very simple function named "fifth" which takes x and returns fifth power of x. No __init__ or class attributes needed.


Finally call your function with number 5 and assign it to variable ans.'''

class Myfunc:
    def fifth(x):
        return x ** 5

ans = Myfunc.fifth(3)
print(ans)