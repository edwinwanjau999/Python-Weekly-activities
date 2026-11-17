#Open customers.txt in read mode ('r')
file = open("customers.txt", "r")

#Read the contents of the file
file_contents = file.read()

#Display the contents on the screen
print("--- Customer Information Records ---")
print(file_contents)

#Close the file using close()
file.close()
