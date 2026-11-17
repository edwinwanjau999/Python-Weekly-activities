#Define a function named calculate_bill() accepting units consumed and cost per unit
def calculate_bill(units_consumed, cost_per_unit):
    bill = units_consumed * cost_per_unit
    return bill


# v. Ask the user to enter the units consumed and cost per unit
units_input = input("Enter the units consumed: ")
cost_input = input("Enter the cost per unit (e.g., KSh): ")

units_consumed = float(units_input)
cost_per_unit = float(cost_input)

total_bill = calculate_bill(units_consumed, cost_per_unit)

# vii. Display the calculated electricity bill
print("\n--- Electricity Bill Summary ---")
print(f"Units Consumed: {units_consumed:,.1f}")
print(f"Cost Per Unit: {cost_per_unit:,.2f}")
print(f"Total Electricity Bill: {total_bill:,.2f}")
