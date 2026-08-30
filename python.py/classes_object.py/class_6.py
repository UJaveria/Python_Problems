# Add __str__ to BankAccount so print(account) shows "Account balance: $150.00"
#  instead of the default repr.
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

    def __str__(self):
        pass
    
b1 = BankAccount(100)
print(b1.balance)
print(b1.deposite(1000))
print(b1.withdraw(200))