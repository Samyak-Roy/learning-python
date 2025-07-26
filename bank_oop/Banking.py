import Account
import Customer

#creating a customer  Sam
sam = Customer.Customer('Sam', '09-09-2000','male', '123456789012', '123 Main St')
sam_account_number = 'ACC123456789'
print()
#creating an account for Sam and passing the customer object to the account object
sam_account = Account.Account(sam_account_number,'savings',sam)
print()
sam_account.deposit(1000)
print()
sam_account.withdraw(200)
print()
sam_account.display_account_details()
print()
sam_account.transaction_log()
print()
sam_account.withdraw(500)
print()
sam_account.deposit(300)