#Create a dictionary named student containing registration number, student name, course, and year of study
student = {
    "reg_number": "S01/12345/2025",
    "student_name": "Jane Doe",
    "course": "Bachelor of Science in Computer Science",
    "year_of_study": 2
}

#Display the student's name and course using their dictionary keys
print("--- Initial Student Information ---")
print("Student Name:", student["student_name"])
print("Course:", student["course"])

student["year_of_study"] = 3

student["email"] = "jane.doe@university.ac.ke"

print("\n--- Complete Updated Student Dictionary ---")
print(student)
