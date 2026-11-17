#Create a class named Product with attributes and methods
class Product:
    def __init__(self, name, code, price, quantity):
        self.name = name
        self.code = code
        self.price = price
        self.quantity = quantity

    def calculateStockValue(self):
        """Calculates: Stock Value = Price × Quantity"""
        return self.price * self.quantity

    def displayProduct(self):
        """Displays product information and individual stock value."""
        stock_value = self.calculateStockValue()
        print(f"Code: {self.code:<10} | Name: {self.name:<22} | Price: KSh {self.price:<9,.2f} | Qty: {self.quantity:<5} | Value: KSh {stock_value:,.2f}")


if __name__ == "__main__":
    #Store the objects in a list
    products_list = []
    
    print("=== Supermarket Inventory Management Portal ===")
    print("Please enter information for at least three products.\n")
    
    count = 0
    #Create at least three product objects dynamically via user input
    while count < 3:
        print(f"--- Product Entry {count + 1} of 3 ---")
        name = input("Enter product name: ")
        code = input("Enter product code (e.g., PRD-001): ")
        
        try:
            price_input = input("Enter product price (KSh): ")
            price = float(price_input)
            if price < 0:
                raise ValueError("Price cannot be negative.")
                
            qty_input = input("Enter quantity in stock: ")
            quantity = int(qty_input)
            if quantity < 0:
                raise ValueError("Quantity cannot be negative.")

            product_obj = Product(name, code, price, quantity)
            products_list.append(product_obj)
            count += 1
            print("✅ Product registered successfully!\n")
            
        except ValueError as err:
            print(f"❌ Invalid input: {err}. Please enter valid numbers for price and quantity.\n")

    print("\n" + "="*95)
    print("                         SUPERMARKET INVENTORY SUMMARY REPORT")
    print("="*95)

    total_inventory_value = 0.0
    for idx, prod in enumerate(products_list, start=1):
        print(f"[{idx}] ", end="")
        prod.displayProduct()
        total_inventory_value += prod.calculateStockValue()
        
    print("="*95)
    print(f"GRAND TOTAL INVENTORY VALUE: KSh {total_inventory_value:,.2f}")
    print("="*95)

    file = open("inventory.txt", "w")
    file.write("=== Supermarket Inventory Records ===\n")
    
    for prod in products_list:
        stock_val = prod.calculateStockValue()
        record_line = f"Code: {prod.code} | Name: {prod.name} | Price: KSh {prod.price:.2f} | Qty: {prod.quantity} | Total Value: KSh {stock_val:.2f}\n"
        file.write(record_line)
        
    file.write(f"\nGRAND TOTAL INVENTORY VALUE: KSh {total_inventory_value:.2f}\n")

    file.close()
    print("\nSuccess! Inventory details have been saved to 'inventory.txt' and the file has been securely closed.")
