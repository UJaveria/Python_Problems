# Create BankAccount with balance (default 0) and a deposit(amount) method
class BankAccount :
    def __init__(self,balance=0):
        self.balance = balance

    def deposite(self,amount) :
        new_balance = self.balance
        if amount > 0:
            self.balance += amount
        return self.balance
    
b1 = BankAccount(100)
print(b1.balance)
print(b1.deposite(1000))
