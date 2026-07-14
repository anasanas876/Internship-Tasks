# Task2
class Bank:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        if amount < 0:
            print("Deposit amount cannot be negative.")
        else:
            self.balance += amount
            print("Deposit successful.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance.")
        else:
            self.balance -= amount
            print("Withdrawal successful.")

    def display_balance(self):
        print("Current Balance:", self.balance)


user = Bank(200)

user.deposit(90)
user.withdraw(650)
user.display_balance()