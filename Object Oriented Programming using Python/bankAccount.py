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
        
        
def main():
    # creating object of the BankAccount class 
    obj1 = BankAccount(10000)
    # Check balance in your bank account
    print("Current Balance in your bank account is : " ,obj1.checkBalance())
    
    money = float(input("How much money you want to deposit to your bank account? : "))
    print("I will deposit this amount into bank account!")
    obj1.deposit(money)
    
    print("After dposit, now the Current Balance in your bank account is : " ,obj1.checkBalance())
    
    
    
main()