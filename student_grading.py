#Ask the student to enter their name and examination mark
student_name = input("Enter student name: ")
mark_input = input("Enter examination mark: ")

#Convert the mark to an integer
mark = int(mark_input)

#Check for invalid marks first (below 0 or above 100)
if mark < 0 or mark > 100:
    print("Invalid mark")
else:
    if 70 <= mark <= 100:
        grade = "A"
    elif 60 <= mark <= 69:
        grade = "B"
    elif 50 <= mark <= 59:
        grade = "C"
    elif 40 <= mark <= 49:
        grade = "D"
    else:
        grade = "F"  # Below 40

    #Display the student's name, mark, and grade
    print("\n--- Student Grade Report ---")
    print("Student Name:", student_name)
    print("Mark:", mark)
    print("Grade:", grade)
