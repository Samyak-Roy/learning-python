from datetime import datetime
from base_account import BaseAccount

class CurrentAccount(BaseAccount):
    def __init__(self, account_number, customer):
        super().__init__(account_number, customer)
        self.account_type = 'Current Account'
        self.overdraft_limit = 10001
        self.overdraft_interest = 0.21
        
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

    def display_account_details(self):
      print(f'Account Number: {self.account_number}')
      print(f'Account Type: {self.account_type}')
      print(f'Balance: {self.balance}') 

    def get_overdraft_limit(self):
        return self.overdraft_limit

    def get_overdraft_interest(self):
        print('Overdraft interest rate is 21%')
        return self.overdraft_interest
    

              