# transaction.py
from datetime import datetime

class Transaction:
    def __init__(self, source_account, destination_account, amount):
        self.timestamp = datetime.now()
        self.source_account = source_account
        self.destination_account = destination_account
        self.amount = amount

    def display_transaction_info(self):
        print(f"Timestamp: {self.timestamp}, Source Account: {self.source_account.account_number}, "
              f"Destination Account: {self.destination_account.account_number}, Amount: ${self.amount}")
