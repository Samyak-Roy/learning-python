from base_account import BaseAccount
print('BaseAccount module imported successfully.')
from current_account import CurrentAccount
from savings_account import SavingsAccount
from customer import Customer

Sam = Customer('Sam', '5.2.2000', 'male', '555-1234','ABC Street')
sam_account = SavingsAccount('SA123456', Sam)
sam_account.deposit(1000)
sam_account.withdraw(200)   
sam_account.display_account_details()
print('\n\n')

ABCTrading = Customer('ABCTrading', '6.9.2000', 'n/a', '555-5678','123 Street')
abc_account = CurrentAccount('CA654321', ABCTrading)
abc_account.deposit(10000)
abc_account.withdraw(5000)
abc_account.display_account_details()
print('\n\n')

base_account = BaseAccount('12341234',ABCTrading)
base_account.display_account_details()
base_account.deposit(5000)
abc_account.get_overdraft_interest()

