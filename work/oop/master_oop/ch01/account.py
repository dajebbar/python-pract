# Account class
import string
import random
import json


class Account:
    ''''''
    def __init__(self, fname, lname, sex, birth, balance, password):
        self.fname = fname
        self.lname =lname 
        if not isinstance(balance, (float, int)):
            print(f'Balance {balance} must be a number')
        elif balance < 0:
            print(f'Balance must be poitive')
        else:
            self.balance = balance
        self.sex = sex
        self.birth = birth
        self.password = password

    def deposit(self, value):
        ''''''
        path = 'clients/clients_list'
        with open(path, 'r') as f:
            clients = json.load(f)
        self.balance = clients['balance']
        passwd = input('Enter your password >>> ')
        if passwd == clients['password']:
            if value < 0. or not isinstance(value, (int, float)):
                print('Error! Deposit must be digits and greater than 0')
            else:
                self.balance += value
        else:
            print('Incorrect password!')

    def widthraw(self, value):
        ''''''
        path = 'clients/clients_list'
        with open(path, 'r') as f:
            clients = json.load(f)
        self.balance = clients['balance']
        passwd = input('Enter your password >>> ')
        if passwd == clients['password']:
            if value < 0. or not isinstance(value, (int, float)) or value > self.balance:
                print('Error!')
            else:
                self.balance -= value
        else:
            print('Incorrect password!')

    def get_balance(self):
        ''''''
        path = 'clients/clients_list'
        with open(path, 'r') as f:
            clients = json.load(f)
        passwd = input('Enter your password >>> ')
        if passwd == clients['password']:
            return self.balance
        else:
            print('Incorrect password!')
    def show(self):
        ''''''

    
def create_account():
    ''''''
    new_client = {}
    sex_lst = ['female', 'male', 'unknown']
    print('Welcome to DAJBANK')
    print('-*-' * 12)
    # Enter client firstname and check it's validity
    fname = input('Your first name? >>> ')
    for i in fname:
        if i in string.digits or i in string.punctuation:
            print(f'Error! Your first name {fname} must not contains a digit ')
            fname = input('Re-enter your first name? >>> ')
    # Enter client lastname and check it's validity
    lname = input('Your last name? >>> ')
    for i in lname:
        if i in string.digits or i in string.punctuation:
            print(f'Error! Your last name {lname} must not contains a digit ')
            lname = input('Re-enter your last name? >>> ')
    # Check the validity of birthyear:  
    birth = int(input('Your year of birth? >>> '))
    for i in birth:
        # Must be a digit
        if i not in string.digits:
            print(f'Error! your year of birth must be a digit!')
            birth = int(input('Re-enter your year of birth? >>> '))
    # Must be 4 digits
    if len(list(birth)) != 4:
        print(f'Error! your year of birth must be exactly 4 digit!')
        birth = int(input('Re-enter your year of birth? >>> '))

    # Check the sex
    sex = input('Your sex? Tape [unknown] if you won\'t to declare it >>> ')
    if sex not in sex_lst:
        print(f'Error! sex must be {sex_lst[0]}, {sex_lst[1]} or {sex_lst[-1]}')
        sex = input('Re-enter your sex?  >>> ')
    
    # Create a password
    password = input('Enter a password?[6-12] >>> ')
    if password < 6 or password >= 12:
        print('Password must be grater than 6 char and lower than 12')
        password = input('Re-enter a password? >>> ')
    
    if fname and lname and birth and sex:
        new_client['fname'] = fname
        new_client['lname'] = lname
        new_client['birth'] = birth
        new_client['sex'] = sex
        new_client['id'] = generate_client_id()
        new_client['password'] = password

    return new_client
# Generate new client id
def generate_client_id():
    # digit part contains 4 digits
    digit_part = ''
    # letter part contains 2 letters
    letter_part = ''
    for i in range(4):
        digit_part += random.randint(0,10)
    for i in range(2):
        letter_part += random.choice(string.ascii_letters)
    # return id with 4digits and 2 letters
    return digit_part + letter_part
# Save new client in json file
def save_client(dico):
    with open('clients/clients_list', 'a') as f:
        json.dump(dico, f)
            

def main():
    ''''''
    path = 'clients/clients_list'
    with open(path, 'r') as f:
        clients = json.load(f)
    account_0 = Account(clients)
    choice = ''
    print('Welcome to DAJBANK')
    print('To [C]reate a new account in DAJBANK, please tape "C"')
    print('To [S]how your DAJBANK account total infos , please tape "S"')
    print('To [G]et balance from your DAJBANK account, please tape "G"')
    print('To [D]eposit money in your DAJBANK account, please tape "D"')
    print('To [W]idthraw from your DAJBANK account, please tape "W"')
    print('Please, tape "Q" to [Q]uit!')

    


    

if __name__=='__main__':
    main()
