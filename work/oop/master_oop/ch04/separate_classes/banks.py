from acount import *


class Bank:
    def __init__(self):
        # A dictionary when the customers account will be putted.
        self.clients = {}
        # Increment position of customer in dictionary
        self.next_client_position = 0
    
    def create_account(self, name, balance, password):
        # create an account for customer
        client_account = Account(name, balance, password)
        # give a customer a position in client dictionary that will be incremented
        new_client_position = self.next_client_position
        # Put account in the exact position in the dictionary
        self.clients[new_client_position] = client_account
        # Increment to prepare for next account to be created
        self.next_client_position += 1
        # Return the position
        return new_client_position
    
    def open_account(self):
        print('*** Open Account ***')
        # Get the name of client
        client_name = input('What is the name for the new user account? >> ')
        # Get the password
        client_password = input('What password would you want to use for this account? >> ')
        # Get the balance that is a positive number
        
        try:
            client_balance = float(input('What is the starting balance for this account? >>'))
        except ValueError:
            raise AbortTransaction('The balance must be a number')
        # Create an account and get the number position
        client_account_number = self.create_account(client_name, client_balance, client_password)
        print('Your new account number is:', client_account_number)
        print()
    
    def close_account(self):
        print('*** Close Account ***')
        
        # Get the exact position number of costumer in the dictionary
        try:
            client_account_number = int(input('What is your account number? >> '))
        except ValueError:
            raise AbortTransaction('Incorrect account number')
        if not isinstance(client_account_number, int):
                raise AbortTransaction(f'{client_account_number} does not exist')
        # Get the exact account for the exact customer
        this_client_account = self.clients[client_account_number] 
        # Check the password 
        client_password = input('What is your password? ')
        # If the password is correct we get the balance
        # if client_password == this_client_account.password:
        the_balance = this_client_account.get_balance(client_password)
        # If the balance is greater than zero we returned it to the customer
        if the_balance is not None:
            print(f'You had, {the_balance}, in your account, which is being returned to you.')
            # Remove user's account from the dictioary of accounts
            del self.clients[client_account_number]
            print('Your account is now closed.')
    
    def balance(self):
        print('*** Get Balance ***')
        try:
            # Get the position of the client account
            client_account_number = int(input('Please enter your account number:  >> '))
        except ValueError :
            raise AbortTransaction('Incorrect account number')
        # Check if the position is correct
        if not isinstance(client_account_number, int):
                # In case of wrong position
                raise AbortTransaction(f'{client_account_number} does not exist')
        # Get the password
        client_password = input('Please enter the password: >> ')
        # Check if the password is correct
        # if client_password != self.clients[client_account_number].password:
        #     client_password = input('Wrong password! Please re-enter the password again: >> ')
        # Get all account
        this_client_account = self.clients[client_account_number] 
        # Check the balance
        the_balance = this_client_account.get_balance(client_password)
        if the_balance is not None:
            print('Your balance is: ', the_balance)
                

    
    def deposit(self):
        print('*** Deposit ***')
        try:
            account_num = int(input('Please enter the account number: '))
            client_account = self.clients[account_num]
            deposit_amount = float(input('Please enter amount to deposit: '))
        except ValueError:
            raise AbortTransaction('Some error(s) has encountred!')
        if account_num not in list(self.clients.keys()):
            print(f'{account_num} does not exist!')
        if not isinstance(account_num, int):
            # In case of wrong position
            raise AbortTransaction(f'{account_num} is wrong!')
        if not isinstance(deposit_amount, (float, int)):
            raise AbortTransaction(f'{deposit_amount} is wrong!')

                 
        client_password = input('Please enter the password: ')
        if client_password != self.clients[account_num].password:
                client_password = input('Wrong password! Please re-enter the password again: >> ')
        # client_account = self.clients[account_num]        
        the_balance = client_account.deposit(deposit_amount, client_password)
        if the_balance is not None:
            print('Your new balance is:', the_balance)
                
    def withdraw(self):
        print('*** Withdraw ***')
        try:
            account_num = int(input('Please enter the account number: '))
            client_account = self.clients[account_num] 
            withdraw_amount = float(input('Please enter amount to withdraw: '))
        except ValueError:
            raise AbortTransaction('Some error(s) has encountred!')
        if account_num not in list(self.clients.keys()):
            print(f'{account_num} does not exist!')
        if not isinstance(account_num, int):
            # In case of wrong position
            raise AbortTransaction(f'{account_num} is wrong!')
        client_password = input('Please enter the password: ')
        if client_password != self.clients[account_num].password:
                client_password = input('Wrong password! Please re-enter the password again: >> ')     
        the_balance = client_account.withdraw(withdraw_amount, client_password)
        if the_balance is not None:
            print('Your new balance is:', the_balance)
                
    
    def show(self):
        print('*** Show ***')
        for client_account_number in self.clients:
            this_client_account = self.clients[client_account_number]
            print('   Account number:', client_account_number)
            this_client_account.show()
    
    def bankInfo(self):
        print('Hours: 9 to 5')
        print('Address: 123 Main Street, Anytown, USA')
        print('Phone:  (650) 555-1212')
        print('We currently have', len(self.clients), 'account(s) open.')
    
    


        

