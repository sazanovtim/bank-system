# account.py
class Account:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance
        self.transactions = []

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return True
        else:
            print("Insufficient funds.")
            return False

    def add_transaction(self, transaction):
        self.transactions.append(transaction)

    def display_account_info(self):
        print(f"Account Number: {self.account_number}, Balance: ${self.balance}")
        print("Transactions:")
        for transaction in self.transactions:
            transaction.display_transaction_info()
            print()
