#Store the initial account balance as KSh 50,000
balance = 50000
print(f"Welcome! Your current account balance is: KSh {balance:,}")

#Ask the customer to enter the withdrawal amount
amount_input = input("Enter the withdrawal amount (must be a multiple of KSh 500): ")

# Convert the amount to an integer
try:
    withdrawal_amount = int(amount_input)
    
    #Check conditions:
    if withdrawal_amount <= 0:
        print("Error: The withdrawal amount must be greater than zero.")
        
    elif withdrawal_amount > balance:
        print("Error: Insufficient funds. The withdrawal amount exceeds your current account balance.")
        
    elif withdrawal_amount % 500 != 0:
        print("Error: Invalid amount. The withdrawal amount must be a multiple of KSh 500.")
        
    else:
        balance -= withdrawal_amount
        
        #Display the remaining balance
        print("\n--- Transaction Successful ---")
        print(f"Amount Withdrawn: KSh {withdrawal_amount:,}")
        print(f"Remaining Balance: KSh {balance:,}")

except ValueError:
    print("Error: Please enter a valid numeric value for the amount.")
