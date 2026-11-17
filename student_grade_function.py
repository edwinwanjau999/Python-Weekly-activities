#Define a function named calculate_grade(mark) that accepts the mark as a parameter
def calculate_grade(mark):
    if 70 <= mark <= 100:
        return "A"
    elif 60 <= mark <= 69:
        return "B"
    elif 50 <= mark <= 59:
        return "C"
    elif 40 <= mark <= 49:
        return "D"
    else:
        return "F"  # Below 40 (iv. Return the appropriate grade)


mark_input = input("Enter the student's mark: ")
mark = int(mark_input)

grade = calculate_grade(mark)

print("\n--- Student Grade Report ---")
print(f"Mark: {mark}")
print(f"Grade: {grade}")
