# customer.py
class Customer:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.accounts = []

    def add_account(self, account):
        self.accounts.append(account)

    def display_customer_info(self):
        print(f"Customer Name: {self.name}, Email: {self.email}")
        print("Accounts:")
        for account in self.accounts:
            account.display_account_info()
            print()
