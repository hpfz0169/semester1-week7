class Transaction:
    def __init__(self, transaction_id, amount, date, description):
        self.transaction_id = transaction_id
        self.amount = amount
        self.date = date
        self.description = description

    def __str__(self):
        return f"Transaction {self.transaction_id} on {self.date} for {self.amount:.2f} for {self.description}"
    
rent_transaction = Transaction("T123", 500, "2023-11-05", "Rent")
print(rent_transaction)
    
# define the __init__ method with the following attributes:
# * transaction id (integer)
# * amount (float)
# * date (yyyy-mm-dd string)
# * description (string)

# define the __str__ method in the following format:
# "Transaction T123 on 2023-11-05 for £500.00 for Rent"
# using an f-string
# Test the class for several different objects
