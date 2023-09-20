class BankAccount:
  def __init__(self,account_number,account_holder_name,initial_balance=0.0):
    self.__account_number=account_number
    self.__account_holder_name=account_holder_name
    self.__account_balance=initial_balance
  def deposit(self,amount):
    if amount > 0:
     self.__account_balance += amount
     print("deposited ₹{}. new balance: ₹{}".format(amount,self.__account_balance))
  
    else:
     print("invalid deposit amount.")
  def withdraw(self,amount):
    if amount >0 and amount <= self.__account_balance:
      self.__account_balance -=amount
      print("withdraw ₹{}. new balance: ₹{}".format(amount,self.__account_balance))
    else:
      print("invalid withdraw amount or insufficient balance:")
  def display_balance(self):
      print("account balance for {} (account #{}: ₹{}".format( self.__account_holder_name,self.__account_number, self.__account_balance)) 
account=BankAccount(account_number="2345678901",account_holder_name="priya",initial_balance=7000.0)

account.display_balance()
account.deposit(1000.0)
account.withdraw(500.0)
account.display_balance()
