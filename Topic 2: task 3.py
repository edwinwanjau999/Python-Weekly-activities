
# Create and assign values to employee variables
employee_name = "Matthew Mwangi"
employee_age = 25
employee_salary = 50000.00
employee_active = True

# Display employee information using f-string formatting
print("--- Employee Information ---")
print(f"Employee Name: {employee_name}")
print(f"Employee Age: {employee_age}")
print(f"Employee Salary: {employee_salary:.2f}")
print(f"Employee Active: {employee_active}")

# Convert a number to a string before concatenating
age_message = "Employee age is " + str(employee_age)
print(age_message)
