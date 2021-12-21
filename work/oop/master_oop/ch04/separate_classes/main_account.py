from banks import *


o_bank = Bank()
def main():
    # Fuction to quit app
    def other(*args, **kwargs):
        print('Good bye')
    # create some accounts
    acc_1 = o_bank.create_account('josé petri', 120, 'jose123')
    print(f'José\'s account number is: {acc_1}')
    acc_2 = o_bank.create_account('maria delporto', 3000, 'maria123')
    print(f'Maria\'s account number is: {acc_2}')

    # Dictionary containing what to do when calling action
    actions = dict(b=o_bank.balance, c=o_bank.close_account, d=o_bank.deposit, w=o_bank.withdraw, 
                i=o_bank.bankInfo, o=o_bank.open_account, s=o_bank.show, q=other)
    while 1:
        print()
        print('To get an account balance, press b')
        print('To close an account, press c')
        print('To make a deposit, press d')
        print('To get bank information, press i')
        print('To open a new account, press o')
        print('To quit, press q')
        print('To show all accounts, press s')
        print('To make a withdrawal, press w')
        print()

        choice = input('What do you want to do? >> ')[0]
        if choice not in actions.keys():
            print('Sorry, that was not a valid action.  Please try again.')
        else:
            if choice == 'q':
                other()
                break
            actions.get(choice, other)()


if __name__=='__main__':
    main()