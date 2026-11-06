class Bank account:
  def __init__(self, account_number, customer_name, date_of_opening, balance):
    self.account_number = account_number
    self.customer_name = customer_name
    self.date_of_opening = date_of_opening
    self.balance = balance
  def deposit(self, amount):
    self.balance += amount
    return amount
  def withdraw(self, amount):
    if self.balance<amount:
    return "insufficient balance"
    else:
    self.balance -= amount
    return amount
    def check_balance(self):
print(f"Current Balance :"{self.Balance})
  def customer_details(self):
print("---CUSTOMER DETAILS---")
print(f"Customer Name :"{self.customer_name})
print(f"Account Number :"{self.account_number})
print(f"Date of opening :"{self.date_of_opening})
print(f"Balance : "{self.balance})
  if_name_=="_main_":
  my_account =BankAccount(1234, "EDU", "2023-01", 500.0)
print(f"Deposited : {my_account.deposit(200)}")
print(f"Withdraw 1000: {my_account.withdraw(1000)}")
print(f"withdraw 150: {my_account.withdraw(150)}")
  myaccount.check_balance()
  my_account.customer_details()
