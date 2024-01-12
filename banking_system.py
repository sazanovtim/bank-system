# banking_system.py
from customer import Customer
from account import Account
from transaction import Transaction

# Create customers
customer1 = Customer("John Doe", "john@example.com")
customer2 = Customer("Jane Doe", "jane@example.com")

# Create accounts
account1 = Account(1, 1000.0)
account2 = Account(2, 500.0)

# Create transactions
transaction1 = Transaction(account1, account2, 200.0)
account1.add_transaction(transaction1)
account2.add_transaction(transaction1)

# Add accounts to customers
customer1.add_account(account1)
customer2.add_account(account2)

# Display customer information
print("Customer Information:")
customer1.display_customer_info()
print()
customer2.display_customer_info()
