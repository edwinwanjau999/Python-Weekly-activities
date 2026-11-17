#Create a dictionary named inventory containing at least five products and their quantities
inventory = {"Milk": 50,"Bread": 30,"Eggs": 120, "Sugar": 40, "Rice": 25}

print("Initial Inventory:")
print(inventory)

#Display the quantity of a specified product (e.g., Bread)
print("\n--- Checking Specific Product ---")
print(f"Quantity of Bread in stock: {inventory['Bread']}")

#Add a new product to the dictionary
inventory["Flour"] = 60
print("\nAdded 'Flour' (Quantity: 60)")

#Update the quantity of an existing product (e.g., updating Milk stock to 45)
inventory["Milk"] = 45
print("Updated 'Milk' quantity to: 45")

#Remove one product from the dictionary
removed_item = inventory.pop("Sugar")
print(f"Removed '{removed_item}' (Sugar) from the inventory.")

# vi. Display the final inventory
print("\n--- Final Inventory Summary ---")
print(inventory)
