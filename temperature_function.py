#Define a function named convert_temperature() that accepts Celsius as a parameter
def convert_temperature(celsius):
    fahrenheit = (celsius * 9 / 5) + 32
    
    return fahrenheit


# v. Ask the user to enter the temperature in Celsius
celsius_input = input("Enter the temperature in Celsius: ")
celsius = float(celsius_input)

fahrenheit_result = convert_temperature(celsius)

# Display the converted temperature to two decimal places
print("\n--- Temperature Conversion Summary ---")
print(f"Temperature in Celsius: {celsius:.2f}°C")
print(f"Converted Temperature in Fahrenheit: {fahrenheit_result:.2f}°F")
