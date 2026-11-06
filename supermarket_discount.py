# Supermarket Discount Calculation
# Ask the customer to enter the purchase amount
purchase_amount = float(input("Enter total purchase amount (KSh): "))

if purchase_amount >= 10000:
    discount = 0.15 * purchase_amount
else:
    discount = 0

final_amount = purchase_amount - discount

# Display the results
print("\n--- Supermarket Purchase Details ---")
print("Purchase Amount: KSh", purchase_amount)
print("Discount: KSh", discount)
print("Final Amount: KSh", final_amount)
