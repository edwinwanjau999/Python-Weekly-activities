#Create a tuple named customer containing name, ID, telephone number, and email address
customer = ("Edu", "001", "254-1234", "edu@gmail.com")

#  Display the complete tuple
print("Complete Customer Tuple:")
print(customer)

#Access and display the customer's name and telephone number using their indexes
print("\n--- Accessing Elements ---")
print("Customer Name:", customer[0])
print("Telephone Number:", customer[2])

# iv. Display the number of items in the tuple using len()
print("\nNumber of items in the tuple:", len(customer))

# v. Attempt to modify the customer's telephone number
print("\n--- Attempting Modification ---")
try:
    customer[2] = "254-9876"
except TypeError as e:
    print("Error caught during modification attempt:", e)
