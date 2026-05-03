#project 1
class BankAccount:
    def __init__(self,name,balance=0):
        self.name=name
        self.balance=balance
    def deposit(self,amount):
        self.balance=self.balance+amount
        print(f'Hi,{self.name} your deposit of RS. {amount} is successful')
        print(f'your current balance is Rs. {self.balance}')
    def withdraw(self,withdraw_amount):
        if withdraw_amount<=(self.balance):
            self.balance=self.balance-withdraw_amount
            print(f'Hi,{self.name} your Rs.{withdraw_amount} withdraw is successful')
            print(f'your current amount is Rs.{self.balance}')
        else:
            print(f'please enter valid amount')
        
obj1=BankAccount('ram',1000)
obj1.withdraw(5000)