#Ask the employee to enter name, years of service, and performance rating
employee_name = input("Enter employee name: ")
years_input = input("Enter years of service: ")
rating_input = input("Enter performance rating: ")

#Convert the years of service and performance rating to integers
years_of_service = int(years_input)
performance_rating = int(rating_input)

#Use logical operators to check whether years of service >= 3 AND performance rating >= 4
qualifies = (years_of_service >= 3) and (performance_rating >= 4)

#Display the employee's details and eligibility result
print("\n--- Employee Details ---")
print("Employee Name:", employee_name)
print("Years of Service:", years_of_service)
print("Performance Rating:", performance_rating)

print("\n--- Bonus Eligibility Result ---")
if qualifies:
    # iv. If the employee qualifies
    print("Employee qualifies for a bonus")
else:
    # v. Otherwise
    print("Employee does not qualify for a bonus")
