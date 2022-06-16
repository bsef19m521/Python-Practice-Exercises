class BankAccount:
    # The __init__ method accepts account's balance as argument and assigns it to the __balance attribute
    def __init__(self,bal):
        self.__balance =bal
        
    # deposit method add balance into the bank account
    def deposit(self, amount):
        self.__balance += amount
        
    # withdraw method withdraws balance from the account
    def withdraw(self, amount):
        if self.__balance > amount:
            self.__balance -= amount
        else:
            print("Your balance is insufficient to withdraw from bank account!")
    
    # checkBalance method returns the current balance in the bank account
    def checkBalance(self):
        return self.__balance
        
        
