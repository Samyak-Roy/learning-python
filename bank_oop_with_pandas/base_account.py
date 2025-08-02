
from datetime import datetime

class BaseAccount:
    def __init__(self,account_number,customer):
        self.account_number = account_number
        self.balance = 0
        self.customer = customer
        self.transactions = []
    
    def withdraw(self,amount):
      if amount > 0:
        if self.balance > 0 and self.balance >= amount:
          self.balance -= amount
          print(f'{amount} has been deducted.')
          print(f'Your current balance is {self.balance}')
          now = datetime.now()
          debit_tx = (now, 'debit', amount, 'balance', self.balance)
          self.transactions.append(debit_tx)
        else:
          print('Insufficient balance. Add funds.')
      else:
        print('Invalid amount. Please enter a positive value.')
    
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
      print(f'Account Type: Base Account')
      print(f'Balance: {self.balance}') 

    def transaction_log(self):
      for tx in self.transactions:
        print(tx)

    def set_transaction_log(self,transaction_log):
      self.transactions.append(transaction_log)

    def __str__(self):
        return f"Account Number: {self.account_number}, Customer: {self.customer.name}, Balance: {self.balance}"
