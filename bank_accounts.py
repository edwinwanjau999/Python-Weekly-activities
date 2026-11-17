#Create a parent class named Account
class Account:
    def __init__(self, account_number, balance):
        # Parent attributes: Account number and Balance
        self.account_number = account_number
        self.balance = balance

    #Include a method named displayAccount()
    def displayAccount(self):
        print(f"Account Number : {self.account_number}")
        print(f"Current Balance: KSh {self.balance:,.2f}")


#Create a child class named SavingsAccount that inherits from Account
class SavingsAccount(Account):
    def __init__(self, account_number, balance, interest_rate):
        
        super().__init__(account_number, balance)
        
        #Add Interest rate to the SavingsAccount class
        self.interest_rate = interest_rate

    #Include a method named calculateInterest()
    def calculateInterest(self):
        # Formula: Interest = Balance × Interest Rate / 100
        interest = (self.balance * self.interest_rate) / 100
        return interest

    # Method to display complete savings account details and calculated interest
    def displaySavingsDetails(self):
        print("\n--- Savings Account Profile ---")
        self.displayAccount()
        print(f"Interest Rate  : {self.interest_rate}%")
        earned_interest = self.calculateInterest()
        print(f"Calculated Interest: KSh {earned_interest:,.2f}")


#In the main section
if __name__ == "__main__":
    # Create a SavingsAccount object with account number, balance, and interest rate
    my_savings = SavingsAccount(
        account_number="SAV-889922", 
        balance=250000.00, 
        interest_rate=6.5
    )

    # Display the account details and calculated interest
    my_savings.displaySavingsDetails()
