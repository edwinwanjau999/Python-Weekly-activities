#Create a dictionary named employees containing at least five employees and their salaries
employees = {"Edu": 75000,"Jack": 82000,"JOHNTE": 65000,"Diana": 90000,  "LORNA": 70000}

print("--- Initial Employee Records ---")
for name, salary in employees.items():
    print(f"Employee: {name:<10} | Salary: KSh {salary:,}")

employees["Bob"] = 88000
print("\n[Update] Edu's salary has been updated to KSh 88,000.")

#Add a new employee and salary
employees["Fiona"] = 78000
print("[Addition] Added new employee Fiona with a salary of KSh 78,000.")

#Calculate and display the total salary payable to all employees
total_salary = sum(employees.values())

print("\n--- Salary Summary ---")
print(f"Total Salary Payable to All Employees: KSh {total_salary:,}")
