class BankAccount:
    def __init__(self, accountNumber, name, balance):
        self.accountNumber = accountNumber
        self.name = name
        self.balance = balance

    def deposit(self, d):
        self.balance = self.balance + d

    def withdrawal(self, w):
        if self.balance < w:
            print('Insufficient balance.')
        else:
            self.balance = self.balance - w

    def bank_fees(self):
        self.balance = (95/100) * self.balance

    def display(self):
        print('Account number:', self.accountNumber)
        print('Account name:', self.name)
        print('Account balance:', self.balance)


new_acc = BankAccount(21345432, 'Miko', 75000)
new_acc.withdrawal(300)
new_acc.display()
