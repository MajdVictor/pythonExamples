class Account():

    def __init__(self,owner,balance):
        self.owner = owner
        self.balance = balance

    def __str__(self):
        return f'Account Owner: {self.owner}\nAccount Balance: ${self.balance}'

    def deposit(self,amount):
        self.balance += amount
        print('Deposit Accepted!')
    
    def withdraw(self,amount):
        if amount > self.balance:
            print('Funds Unvailable!')
        else:

            self.balance -= amount
            print('Withdrawal Accepted!')


acct1 = Account('Jose',100)
acct1.withdraw(500)