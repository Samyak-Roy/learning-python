from base_account import BaseAccount
from current_account import CurrentAccount
from savings_account import SavingsAccount
from customer import Customer
import openpyxl as px
import pandas as pd 
print('All modules initialized successfully.')

filelocation1 = r'E:\Coding\learning-python-2025\learning-python\bank_oop_with_pandas\test_account_data\account_ACCT0001.xlsx'

ACCT0001_accounts = pd.read_excel(filelocation1, sheet_name='Account Details',engine='openpyxl')
account_id = ACCT0001_accounts.iloc[0,1]
account_name = ACCT0001_accounts.iloc[1,1]
account_DOB = ACCT0001_accounts.iloc[2,1]
customer = Customer( account_name, account_DOB,None, None, None)
print(customer)
account = SavingsAccount(account_id, customer)
print(account)

print('\n')
ACCT0001_transactions = pd.read_excel(filelocation1, sheet_name='Transactions',engine='openpyxl')
#print(ACCT0001_transactions.head(10))
last_balance = 0
for index, row in ACCT0001_transactions.iterrows():
    transaction = (row['Date'], row['Type'], row['Amount'], row['Balance'])
    account.set_transaction_log(transaction)
    last_balance = row['Balance']

account.balance = last_balance
account.transaction_log()
print(account.balance)