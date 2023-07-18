class Account:

    def __init__(self, tittle, balance):
        self.tittle = tittle
        self.balance = balance
        # write your code here
        

class SavingsAccount(Account):

    def __init__(self, tittle, balance, interestRate):
        super().__init__(tittle, balance)
        self.interestRate=interestRate

obj = Account("Ashish", 5000)
obj2= SavingsAccount("Ashish", 5000, 5)

# Accessing the properties of the SavingsAccount class
print(obj2.tittle)  
print(obj2.balance)  
print(obj2.interestRate) 