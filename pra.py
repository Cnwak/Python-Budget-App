
# BUDGET CLASS CREATED
class Budget:
  def __init__(self,category: str,balance: int):
    self.category = category
    self.balance = balance


# DEPOSIT FUNCTION
  def deposit(self,sub_category,amount_added):
    self.balance += amount_added
    return "You deposited ₦%d for the purchase of %s(%s)"%(self.balance,self.category,sub_category)


# WITHDRAWAL FUNCTION
  def withdraw(self,sub_category,amount_added):
    self.balance -= amount_added
    if (self.balance < 0):
      # TO CANCEL OUT THE NEGATIVE BALANCE, I MULITPLIED BY -1
      self.balance *= -1
      return "There is no money to withdraw from.You will be owing ₦%d"%self.balance
    else:  
      return "You withdrew ₦%d for the purchase of %s(%s)"%(self.balance,self.category,sub_category)

#GET BALANCE 
  def get_balance(self):
    return "Your balance is ₦%d" %self.balance


# TRANSFER METHOD
  @staticmethod
  def transfer(fro,to,amount_added: int):
    if(amount_added > 0) and (amount_added <= fro.balance):
      fro.balance -= amount_added
      to.balance += amount_added
      return "You succesfully transferred ₦%d"%(amount_added)
    else:
      print("Sorry, an error was encountered. Check the transfer amount or the transfer source.")


# INSTANTIATED OBJECTS
budget_one = Budget('Food',50) 
budget_two = Budget('Entertainment',50)    
budget1_three = Budget('Clothes',50)    




#TEST CODES 

# print(Budget.transfer(budget_one,budget_two,20))
# print(budget_one.deposit('Beans',100))
# print(budget_one.deposit('Beans',100))
# print(budget_one.deposit('Beans',100))
# print(budget_one.withdraw('Beans',200))
# print(budget_one.withdraw('Beans',100))
# print(budget_two.withdraw('Dance',700))
# print(budget_two.withdraw('Dance',100))
# print(budget_one.get_balance())
# print(budget_two.get_balance())




