# Printing account balance using class and methods

class Account:
    def __init__(self, account_no, balance):
        self.account_no = account_no
        self.balance = balance
    
    #debit method
    def debit(self, amount):
        self.balance -= amount
        print(f'Rs. {amount} was debited')
        print("Total Balance is ",self.get_balance())

    # credit method
    def credit(self, amount):
        self.balance += amount
        print(f'Rs. {amount} was credited')
        print("Total Balance is ",self.get_balance())
        
    # get balance
    def get_balance(self):
        return self.balance
    

acc1 = Account("1001", 10000)
# acc2 = Account("1002", 200000)
acc1.debit(1000)
acc1.credit(50000)