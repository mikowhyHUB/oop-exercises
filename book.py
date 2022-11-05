 #Define a Book class with the following attributes: Title, Author (Full name), Price.
#Define a constructor used to initialize the attributes of the method with values entered by the user.
#Set the View() method to display information for the current book.
#Write a program to testing the Book class.

class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price
    def view(self):
        print('Name of the book:', self.title)
        print('Author:', self.author)
        print('Price of the book:', self.price)

book1 = Book('The Witcher', 'Sapkowski', '39,99zł')

print(book1.view())