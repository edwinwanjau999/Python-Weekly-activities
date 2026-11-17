#Create a class named BankAccount
class BankAccount:
    def __init__(self, account_number, customer_name, balance=0.0):
        # Data members
        self.account_number = account_number
        self.customer_name = customer_name
        self.balance = balance

    #Include public methods
    def deposit(self, amount):
        """To add money to the account balance"""
        if amount > 0:
            self.balance += amount
            print(f"Successfully deposited KSh {amount:,}.")
        else:
            print("Deposit amount must be greater than zero.")

    def withdraw(self, amount):
        """To deduct money from the account balance"""
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Successfully withdrew KSh {amount:,}.")
        else:
            print("Error: Invalid withdrawal amount or insufficient funds.")

    def displayAccount(self):
        """To display account information and current balance"""
        print("\n--- Bank Account Information ---")
        print(f"Account Number : {self.account_number}")
        print(f"Customer Name  : {self.customer_name}")
        print(f"Current Balance: KSh {self.balance:,}")


#In the main section
if __name__ == "__main__":
    
    customer_account = BankAccount("ACC-987654", "Alice Wanjiru", 10000.00)

    customer_account.displayAccount()

    print("\n--- Transaction: Deposit ---")
    customer_account.deposit(5000)

    print("\n--- Transaction: Withdrawal ---")
    customer_account.withdraw(2000)

    customer_account.displayAccount()
