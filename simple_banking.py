#Create a class named BankAccount with account number, customer name, and balance
class BankAccount:
    def __init__(self, account_number, customer_name, balance):
        self.account_number = account_number
        self.customer_name = customer_name
        self.balance = balance

    #Deposit money method
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"✅ Successfully deposited KSh {amount:,.2f}.")
        else:
            print("❌ Deposit amount must be greater than zero.")

    #Withdraw money method ensuring a customer cannot withdraw more than available balance
    def withdraw(self, amount):
        if amount <= 0:
            print("❌ Withdrawal amount must be greater than zero.")
        elif amount > self.balance:
            print(f"❌ Withdrawal Failed: Insufficient funds! Current balance is KSh {self.balance:,.2f}.")
        else:
            self.balance -= amount
            print(f"✅ Successfully withdrew KSh {amount:,.2f}.")

    #Display account details method
    def displayAccount(self):
        print(f"Account No: {self.account_number:<12} | Customer: {self.customer_name:<18} | Balance: KSh {self.balance:,.2f}")


#Use a function named performTransaction() to process a deposit or withdrawal
def performTransaction(account):
    print(f"\n--- Transaction Portal for {account.customer_name} ({account.account_number}) ---")
    print("1. Deposit")
    print("2. Withdraw")
    choice = input("Enter your choice (1 for Deposit, 2 for Withdraw): ")
    
    if choice not in ('1', '2'):
        print("❌ Invalid transaction option selected.")
        return

    try:
        amount_input = input("Enter transaction amount (KSh): ")
        amount = float(amount_input)
        
        if choice == '1':
            account.deposit(amount)
        elif choice == '2':
            account.withdraw(amount)
            
    except ValueError:
        print("❌ Error: Non-numeric amount entered. Please enter a valid number.")


if __name__ == "__main__":
    # vi. Create at least two bank account objects
    account1 = BankAccount("ACC-5001", "Grace Wanjiku", 25000.00)
    account2 = BankAccount("ACC-5002", "Brian Kiprop", 12000.00)

    print("=== Initial Accounts Summary ===")
    account1.displayAccount()
    account2.displayAccount()

    performTransaction(account1)
    performTransaction(account2)

    print("\n" + "="*65)
    print("                 UPDATED ACCOUNT BALANCES")
    print("="*65)
    account1.displayAccount()
    account2.displayAccount()
    print("="*65)

    file = open("accounts.txt", "w")
    file.write("=== Bank Account Management System Records ===\n")
    
    active_accounts = [account1, account2]
    for acc in active_accounts:
        record_line = f"Account No: {acc.account_number} | Customer: {acc.customer_name} | Final Balance: KSh {acc.balance:.2f}\n"
        file.write(record_line)
        
    file.close()
    print("\nSuccess! Account details and updated balances have been saved to 'accounts.txt' and the file has been securely closed.")
