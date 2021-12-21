# Define a custom exception
class AbortTransaction(Exception):
    '''raise this exception to abort a bank transaction'''
    pass

class Account:
    def __init__(self, name, balance, password):
        self.name = name
        if not isinstance(balance, (int, float)):
            raise AbortTransaction('Balance must be a number')
        elif balance < 0:
            raise AbortTransaction('Balance must be positive')
        else:
            self.balance = balance
        self.password = password
    
    def deposit(self, amount_to_deposit, password):
        if password != self.password:
            raise AbortTransaction('Sorry, incorrect password')
            return None
        
        if amount_to_deposit < 0:
            raise AbortTransaction('You cannot deposit a negative amount')
            return None
        
        self.balance += amount_to_deposit
        print(f'deposit done!- {self.name} account\'s')
        return self.balance
    
    def withdraw(self, amount_to_withdraw, password):
        if password != self.password:
            raise AbortTransaction('Incorrect password for this account')
            return None
        if amount_to_withdraw < 0:
            raise AbortTransaction('You cannot withdraw a negative amount')
            return None
        if amount_to_withdraw > self.balance:
            raise AbortTransaction('You cannot withdraw more than you have in your account')
            return None
        
        self.balance -= amount_to_withdraw
        print(f'withdraw done!- {self.name} account\'s')
        return self.balance
    
    def get_balance(self, password):
        if password != self.password:
            raise AbortTransaction('Sorry, incorrect password')
            return None
        return self.balance
    
    # Added for debugging
    def show(self):
        print('       Name:', self.name)
        print('       Balance:', self.balance)
        print('       Password:', self.password)
        print()


def main():
    account1 =  Account('Joe Schmoe', 1000, 'magic')
    new_deposit = account1.deposit(500, 'magic')
    account1.show()

if __name__=='__main__':
    main()