''' Banking system:
paretn class - user
- holds details about an usr
- has a function to show user details
child class - bank
- stores details about the account balance
- stores details about the amount
allows for deposits, withdraws, view balance'''


class User:
    def __init__(self, name, acc_number):
        self.name = name
        self.acc_number = acc_number
        pass

    def show_info(self):
        print('Name of the account owner: ', self.name)
        print('Account number: ', self.acc_number)


class Bank(User):
    def __init__(self, name, acc_number):
        super().__init__(name, acc_number)
        self.balance = 0

    def deposit(self, amount):
        self.amount = amount
        self.balance += amount
        print('The balance has changed for the amount of: ',
              self.amount, 'The balance is: ', self.balance)

    def withdraw(self, amount):
        self.amount = amount
        if self.balance - amount > 0:
            self.balance -= amount
            print('The balance has changed for the amount of: ',
                  self.amount, 'The balance is: ', self.balance)
        else:
            print('Not enough resources')

    def view_balance(self):
        print('The balance is: ', self.balance)


user1 = User('Mikołaj S', 234560000234)
user2 = Bank('Jon', 123515151)
user2.deposit(100)
user2.deposit(540)
user2.withdraw(400)
user2.view_balance()
