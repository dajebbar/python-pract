class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
    
    def deposit(self, depo):
        if isinstance(depo, (int,float)) and depo > 0:
            self.balance += depo
            return "Deposit Accepted"
        return "Deposit Not Accepted"
    
    def withdraw(self, amount):
        if isinstance(amount, (int,float)) and  0 < amount <= self.balance:
            self.balance -= amount
            return "Withdrawal Accepted"
        return "Funds Unavailable!"
    
    def __str__(self):
        return f"Account owner:   {self.owner}\nAccount balance: ${self.balance}"
    

acct1 = Account('Bob',100)

print(acct1)
print(acct1.owner)
print(acct1.balance)
print(acct1.deposit(50))
print(acct1.balance)
print(acct1.withdraw(75))
print(acct1.balance)
print(acct1.withdraw(500))

