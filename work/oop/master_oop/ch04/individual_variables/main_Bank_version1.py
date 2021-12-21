# Test program using accounts
# Version 1, using explicit variables for each Account object

# Bring in all the code from the Account class file
from acount import *

# Create two accounts
oJoesAccount = Account('Joe', 100, 'JoesPassword')
print("Created an account for Joe")
oJoesAccount.show()

oMarysAccount = Account('Mary', 1230.45, 'MarysPassword')
print("Created an account for Mary")
oMarysAccount.show()
print()

# Call some methods on the different accounts
print('Calling methods of the two accounts ...')
oJoesAccount.deposit(50, 'JoesPassword')
oMarysAccount.withdraw(345, 'MarysPassword')
oMarysAccount.deposit(100, 'MarysPassword')

# Show the accounts
oJoesAccount.show()
oMarysAccount.show()

# Create another account with information from the user
print()
userName = input('What is the name for the new user account? ')
userBalance = input('What is the starting balance for this account? ')
try:
    userBalance = float(userBalance)
except TypeError as err:
    print(err)
userPassword = input('What is the password you want to use for this account? ')
oNewAccount = Account(userName, userBalance, userPassword)

# Show the newly created user account
oNewAccount.show()

# Let's deposit 100 into the new account
welcome_balance = 100
oNewAccount.deposit(welcome_balance, userPassword)
usersBalance = oNewAccount.get_balance(userPassword)
print()
print(f'After depositing ${welcome_balance} of welcome balance, users balance is:{usersBalance}')

# Show the new account
oNewAccount.show()