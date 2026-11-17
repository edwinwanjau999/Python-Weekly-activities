#Ask the student to enter their age
age_input = input("Enter your age: ")

#Use try...except to handle invalid input
try:
    # ii. Convert the input to an integer
    age = int(age_input)
    
    #If the user enters a valid number, display the success message
    print("Age successfully recorded")
    print(f"Your registered age is: {age}")

#Ensure that the program does not terminate unexpectedly because of invalid input
except ValueError:
    #If the user enters text such as "twenty", display the required error message
    print("Invalid age entered")
