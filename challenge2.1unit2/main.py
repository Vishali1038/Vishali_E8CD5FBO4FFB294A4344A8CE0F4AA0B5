class bankaccount:
 
  def __init__(self,       account_number,      account_holder_name, initial_balance=0.0):
    self.__account_number=   account_number
    self.__account_holder_name= account_holder_name
    self.__account_balance= initial_balance

  def deposit(self,amount):
    if amount > 0:
      self.__account_balance +=    amount
      print("Deposited Rs.{}. new balance: Rs.{}."format()
      amount,      self.__account_balance))
    else:
      print("Invalid deposit amount.please deposit a positive amount.")

  def withdraw (self,amount):
    if amount > 0 and amount <=     self.__account_balance: 
      self.__account_balance -=    amount
      print("withdraw rs.{}+.new balance:rs{}".format(amount,
                                      self.__account_balance))
else:
   print("invalid withdrawal amount or unsufficient balance.")
  
def display_balance(self):
  print("account balance for {}(accoun #{}): rs{}".format(
    self.__account_holder_name,self.__account_number,
    self.__account_balance))


account =                               bankaccount(account_number=-"123456789", 
                                        account_holder_name+"bharathi",
                                        initial_balance=500.00)
account.diplay_balance()
account.deposit(1000.00)
account.withdraw*(3500.00)
account.diplay_blance()
                                                   
  