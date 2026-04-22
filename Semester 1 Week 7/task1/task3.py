class BankAccount:

    def __init__(self, account_number, account_name, account_balance):
        self.account_number = account_number
        self.account_name = account_name
        self.account_balance = account_balance

    def __str__(self):
        return f"Bank account {self.account_number:08d} for {self.account_name} with a balance of {self.account_balance:.2f}"

johns_account = BankAccount(12345678, "John Doe", 1500)
print(johns_account)

# Define the __init__ method with the following attributes
# * account number (8 digit integer)
# * account name (string)
# * account balance (float)

# Define the __str__ method in the following format:
# "Bank account 12345678 for John Doe with a balance of 1500.00"
# Use an f-string such that account number has a fixed width of 8 digits and balance has 2 decimal places 

      
