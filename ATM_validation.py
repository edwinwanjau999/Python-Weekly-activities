#Ask the customer to enter the withdrawal amount
amount_input = input("Enter the withdrawal amount: ")

#Place the conversion operation inside a try block
try:
    #Convert the entered value to an integer
    withdrawal_amount = int(amount_input)
    
    #Display the withdrawal amount when a valid number is entered
    print(f"\nSuccess! Withdrawal amount entered: KSh {withdrawal_amount:,}")

#Use an except block to handle ValueError
except ValueError:
    #Display the specified error message when invalid data is entered
    print("Invalid amount. Please enter a number.")
