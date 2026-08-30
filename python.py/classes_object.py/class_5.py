# Add withdraw(amount) to BankAccount— only if funds are sufficient, else print 
# "Insufficient funds"

class BankAccount :
    def __init__(self,balance=0):
        self.balance = balance

    def deposite(self,amount) :
        new_balance = self.balance
        if amount > 0:
            self.balance += amount
        return self.balance
    
    def withdraw(self,amount) :
        new_balance = self.balance
        if amount > 0 :
            if amount < new_balance :
                self.balance -= amount
            else :
                return "Insufficient balance"
        else :
            return "Invalid Input"
        return self.balance
    
b1 = BankAccount(100)
print(b1.balance)
print(b1.deposite(1000))
print(b1.withdraw(200))