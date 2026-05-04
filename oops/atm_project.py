class Atm:
    def __init__(self,user_name,balance):
        self.user_name=user_name
        self.balance=balance
        self.menu()
    def menu(self):
        user_input=(input("""
              Hi,how can i help you
              1.press 1 to create pin
              2.press 2 to change pin
              3.press 3 to check balance
              4.press 4 to withdraw
              5.press anything to exit
              """))
        if user_input=='1':
            #create pin
            self.create_pin()
        elif user_input=='2':
            #change pin
            self.change_pin()
        elif user_input=='3':
            #check balance
            self.balance_check()
        elif user_input=='4':
            #withdraw
            self.withdraw()
            
        else:
            exit()
    def create_pin(self):
        self.user_pin=input('enter you pin number')
        print(f'hi,{self.user_name} your pin number is {self.user_pin}')
        self.menu()
    def change_pin(self):
        self.old_pin=input('enter your old pin')
        if self.user_pin==self.old_pin:
            self.new_pin=input('enter your new pin')
            self.user_pin=self.new_pin
            print(f'new pin {self.user_pin} is successfully set!!!')
        else:
            print('your old pin is not matched')
        self.menu()
    def balance_check(self):
        self.check_pin=input('enter you pin to check the balance of you account')
        if self.user_pin==self.check_pin:
            print(f'hi,{self.user_name} your current balance is Rs.{self.balance}')
            self.menu()
        else:
            print('entered pin is not matched!!!!!!!')
        self.menu()
    def withdraw(self):
        self.withdraw_check_pin=input('enter you pin to withdraw balance')
        if self.withdraw_check_pin==self.user_pin:
            self.amount=float(input('enter amount to withdraw'))
            if self.balance>=self.amount:
                print(f'hi,{self.user_name} Rs.{self.amount} is successfully withdraw!!!!!!')
                self.balance=self.balance-self.amount
                print(f'your new balance is {self.balance}')
            else:
                print('enter valid amount')
        else:
            print('enter valid pin!!!!!!')
        self.menu()
        
    
        
        
obj=Atm('pappu',1000)