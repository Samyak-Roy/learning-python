from datetime import datetime
from base_account import BaseAccount

class SavingsAccount(BaseAccount):
    def __init__(self,account_number,customer):
        super().__init__(account_number, customer)
        self.account_type = 'Savings Account'
      
    def display_account_details(self):
        print(f'Account Number: {self.account_number}')
        print(f'Account Type: {self.account_type}')
        print(f'Balance: {self.balance}')

    
