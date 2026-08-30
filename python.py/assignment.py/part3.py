class Account :
    def __init__(self,name,balance,account_number):
        self.name = name
        self.balance = balance
        self.account_number = account_number

    def deposite_money(self,amount) :
        new_balance = self.balance
        if amount > 0 :
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

    def display_currentBalance(self) :
        return f"Current balance : {self.balance}"
    

class Customer(Account) :
    def __init__(self, name, balance, account_number):
        super().__init__(name, balance, account_number)

customer1 = Customer("Javeria",50000,23487902)
print(f"After Deposite money : {customer1.deposite_money(5000)}")
print(f"After withdraw money : {customer1.withdraw(7000)}")
print(f"{customer1.display_currentBalance()}")