class bank_account:
        def account(self,account_number,account_holder,initial_balance=0.0):
                self.__account_number = account_number
                self.__account_holder = account_holder
                self.__account_balance = initial_balance
        def deposite(self,amount):
                if amount > 0:
                        self.__account_balance += amount
                        print ("deposited {}. New blance : {} ".format(amount,self.__account_balance))
                else :
                        print ("invalid deposite amount. plaese deposit a positive amount.")
        
        def withdraw(self,amount):
                if amount >0 and amount <= self.__account_balance:
                        self.__account_balance-= amount
                        print("withdrew ",amount,".New balance : ",self.__account_balance)
                else:
                        print("Invalid withdrawal amount or insufficient balance.")
        def display_balance(self):
                print('account holder ',self.__account_holder,'account number',self.__account_number,'account balance',self.__account_balance)
                
                        
account = bank_account()
account.account(account_number =123456789,account_holder="akash",initial_balance=1000.0)
account.display_balance()

ans=input('do you want deposite amount(yes/no):')
if ans == 'yes' :
        account.deposite(int(input('enter your deposite amount :')))
answer=input('do you want withdrew amount(yes/no):')
if answer=='yes':
        account.withdraw(int(input('enter your withdrew amount :')))
account.display_balance()