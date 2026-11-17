#Create a set named categories containing product categories 
categories = {"Electronics","Clothing", "Electronics", "Home & Kitchen", "Books", "Toys",  "Clothing", "Sports"   }  
#Display the set (duplicates are automatically filtered out)
print("Initial Unique Categories Set:")
print(categories)
# Add a new product category using add()
categories.add("Beauty")
#Remove one category using remove()
categories.remove("Toys")
#Display the final set
print("\nFinal Set of Categories:")
print(categories)
