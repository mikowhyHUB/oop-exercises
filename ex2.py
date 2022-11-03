# Create a Python class called BankAccount which represents a bank account, having as attributes: accountNumber (numeric type), name (name of the account owner as string type), balance.
class BankAccount:
    def __init__(self, account_number, name, balance):
        self.account_number = account_number
        self.name = name
        self.balance = balance

# Create a constructor with parameters: accountNumber, name, balance.

# Create a Deposit() method which manages the deposit actions.
    def deposit(self, deposit):
        self.balance = self.balance + deposit
# Create a Withdrawal() method  which manages withdrawals actions.

    def withdrawal(self, withdrawal):
        self.balance = self.balance - withdrawal
# Create an bankFees() method to apply the bank fees with a percentage of 5% of the balance account.

    def bank_fees(self):
        self.balance = (95/100) * self.balance
# Create a display() method to display account details.

    def display(self):
        print('The account number is:', self.account_number)
        print('Name of the account:', self.name)
        print('Balance:', self.balance)


# Give the complete code for the  BankAccount class.
acc = BankAccount(232391222, 'Robert', 231)
acc.display()
acc.withdrawal(30)
acc.display()
