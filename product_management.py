#Create a class named Product with attributes
class Product:
    def __init__(self):
       
        self.product_name = ""
        self.product_code = ""
        self.price = 0.0
        self.quantity = 0

    #Include the specified methods
    def setProductDetails(self, name, code, price, quantity):
        """To assign product information."""
        self.product_name = name
        self.product_code = code
        self.price = price
        self.quantity = quantity

    def calculateStockValue(self):
        """To calculate: Stock Value = Price × Quantity"""
        return self.price * self.quantity

    def displayProductDetails(self):
        """To display product information and stock value."""
        stock_value = self.calculateStockValue()
        print("\n--- Product Information Report ---")
        print(f"Product Name : {self.product_name}")
        print(f"Product Code : {self.product_code}")
        print(f"Price        : KSh {self.price:,.2f}")
        print(f"Quantity     : {self.quantity}")
        print(f"Stock Value  : KSh {stock_value:,.2f}")


#In the main section
if __name__ == "__main__":
    # Create a Product object
    my_product = Product()

    # Set the product details
    my_product.setProductDetails(
        name="Wireless Ergonomic Mouse",
        code="PRD-9021",
        price=1850.00,
        quantity=35
    )

    # Calculate the stock value and display the product details
    my_product.displayProductDetails()
