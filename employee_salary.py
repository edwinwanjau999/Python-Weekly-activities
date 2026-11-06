# Employee Salary Calculation
# Ask the user to enter employee details
employee_name = input("Enter employee name: ")
basic_salary = float(input("Enter basic salary: "))
deduction = float(input("Enter monthly deduction: "))

housing_allowance = 0.10 * basic_salary

gross_salary = basic_salary + housing_allowance

net_salary = gross_salary - deduction

# Display the results
print("\n--- Employee Salary Details ---")
print("Employee Name:", employee_name)
print("Basic Salary:", basic_salary)
print("Housing Allowance:", housing_allowance)
print("Gross Salary:", gross_salary)
print("Monthly Deduction:", deduction)
print("Net Salary:", net_salary)
