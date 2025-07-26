
from datetime import datetime

class CurrentAccount:
    def __init__(self, account_number, customer):
        self.account_number = account_number
        self.balance = 0
        self.overdraft_limit = 10001
        self.customer = customer
        self.transactions = []
        
    def withdraw(self,amount):
      # Check if the amount is positive
      if amount > 0:
        # Check if the balance is sufficient or within overdraft limit
        if self.balance + self.overdraft_limit >= amount:
          self.balance -= amount
          print(f'{amount} has been deducted.')
          print(f'Your current balance is {self.balance}')
          now = datetime.now()
          debit_tx = (now, 'debit', amount, 'balance', self.balance)
          self.transactions.append(debit_tx)
        else:
          print('Insufficient balance. Add funds or check overdraft limit.')
    
    def deposit(self,amount):
      if amount <= 0:
        print('Invalid amount. Please enter a positive value.')
      else:
        self.balance += amount
        print(f'{amount} has been deposited.')
        print(f'Your current balance is {self.balance}')
        now = datetime.now()
        credit_tx = (now, 'credit', amount, 'balance', self.balance)
        self.transactions.append(credit_tx)

    def display_account_details(self):
      print(f'Account Number: {self.account_number}')
      print(f'Account Type: {self.account_type}')
      print(f'Balance: {self.balance}') 

    def transaction_log(self):
      for tx in self.transactions:
        print(tx)
    

    
        