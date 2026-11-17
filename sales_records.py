#Open sales.txt in append mode ('a')
file = open("sales.txt", "a")

#Ask the user to enter product name, quantity sold, and total sales amount
product_name = input("Enter product name: ")
quantity_sold = input("Enter quantity sold: ")
total_amount = input("Enter total sales amount (e.g., KSh): ")

#Write the new sales record to the file
sales_record = f"Product: {product_name} | Quantity Sold: {quantity_sold} | Total Sales: {total_amount}\n"
file.write(sales_record)

file.close()

print("\nSuccess! The new sales record has been appended to 'sales.txt'.")
