#class and objects
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

#constructor(init)
class Customer:
    def __init__(self,name,account_type): #default constructor
        print('Default constructor is called')
        self.name=name
        self.account_type=account_type
        print(f'name:{name} and account_types:{account_type}')
    @classmethod #alternative constructor
    def customer_details(cls,name,account_type):
        print('Alternative constructor is called')
        return cls(name,account_type)
    @classmethod
    def get_name_account_details(cls,data):
        print('Alternative Constructor is called')
        name,account_details=data.split('-')
        return cls(name,account_details) 
    @classmethod
    def get_dict_data(cls,dict_data):
        print('Alternative Constructor is called')
        name=dict_data.get('name')
        account_type=dict_data.get('account_type')
        return cls(name,account_type) 
        
obj2=Customer('ram','saving')
#Alternative constructor :customer details
obj3=Customer.customer_details('shyam','saving')

#note:while calling Alternative constructor the data from Alternative constructor is passed to Default constructor

#Alternative constructor :get_name_account_details
obj4=Customer.get_name_account_details('pappu-saving')

#Alternative constructor :get_dict_data
obj5=Customer.get_dict_data({'name':'Hari','account_type':'Saving'})