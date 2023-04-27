class Customer:
    def __init__(self, name):
        self.name = name


class BankAccount:
    def __init__(self, customer, balance=0):
        self.customer = customer
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount

    def transfer(self, amount, recipient):
        self.withdraw(amount)
        recipient.deposit(amount)
