from savings_account import SavingsAccount
from customer import Customer
import pandas as pd 
import datetime as dt
print('All modules initialized successfully.')

filelocation1 = r'E:\Coding\learning-python-2025\learning-python\bank_oop_with_pandas\test_account_data\account_ACCT0001.xlsx'

ACCT0001_accounts = pd.read_excel(filelocation1, sheet_name='Account Details')
account_id = ACCT0001_accounts.iloc[0,1]
account_name = ACCT0001_accounts.iloc[1,1]
account_DOB = ACCT0001_accounts.iloc[2,1]
customer = Customer( account_name, account_DOB,None, None, None)
print(customer)
account = SavingsAccount(account_id, customer)
print(account)

print('\n')
ACCT0001_transactions = pd.read_excel(filelocation1, sheet_name='Transactions')
#print(ACCT0001_transactions.head(10))
last_balance = 0
for index, row in ACCT0001_transactions.iterrows():
    transaction = (row['Date'], row['Type'], row['Amount'], row['Balance'])
    account.set_transaction_log(transaction)
    last_balance = row['Balance']

account.balance = last_balance
#account.transaction_log()
#print(account.balance)

lst_of_transactions = account.transactions

dict_of_transactions_by_month = {
    'January': [],
    'February': [],
    'March': [],
    'April': [],
    'May': [],
    'June': [],
    'July': [],
    'August': [],
    'September': [],
    'October': [],
    'November': [],
    'December': []
}

#STEP 1: Convert dates to datetime objects and sort transactions by month
for monthly_transaction in lst_of_transactions:
    date_str = monthly_transaction[0]
    date_obj = dt.datetime.strptime(date_str, '%Y-%m-%d')
    month_name = date_obj.strftime('%B')
    dict_of_transactions_by_month[month_name].append(monthly_transaction[3])   

#print(dict_of_transactions_by_month)

#STEP 2: Averaging the balances of each month
avg_monthly_balance_with_interest = {
    'January': [],
    'February': [],
    'March': [],
    'April': [],
    'May': [],
    'June': [],
    'July': [],
    'August': [],
    'September': [],
    'October': [],
    'November': [],
    'December': []
}

sample_interest_rate = 4
for monthly_avg_with_interest in dict_of_transactions_by_month:
    balances = dict_of_transactions_by_month[monthly_avg_with_interest]
    if balances:
        avg_balance = sum(balances) / len(balances)
        avg_balance_with_interest = (avg_balance * (100+sample_interest_rate))/100
        avg_monthly_balance_with_interest[monthly_avg_with_interest] = avg_balance_with_interest
    else:
        avg_monthly_balance_with_interest[monthly_avg_with_interest] = 0
print(avg_monthly_balance_with_interest)


'''
---first take all the dates inside the transaction log and convert them to datetime objects
---then sort the transaction log by month and store in a dictionary
---from the dictionary pull the balance for each month and take average of the balances
---then calculate monthly interest based on the average balance
---finally, add the interest to the account balance
'''