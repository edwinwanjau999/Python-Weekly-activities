#Create a class named Student
class Student:
    def __init__(self, name, reg_number, course, mark):
        self.name = name
        self.reg_number = reg_number
        self.course = course
        self.mark = mark

    #Include methods to calculate the student's grade and display details
    def calculateGrade(self):
        """Calculates grade based on university criteria."""
        if 70 <= self.mark <= 100:
            return "A"
        elif 60 <= self.mark <= 69:
            return "B"
        elif 50 <= self.mark <= 59:
            return "C"
        elif 40 <= self.mark <= 49:
            return "D"
        else:
            return "F"

    def displayDetails(self):
        grade = self.calculateGrade()
        print(f"Name: {self.name:<18} | Reg No: {self.reg_number:<15} | Course: {self.course:<25} | Mark: {self.mark:<5} | Grade: {grade}")


#Use a function named displayStudents() to display all students
def displayStudents(student_list):
    print("\n" + "="*85)
    print("                   UNIVERSITY STUDENT RECORDS SUMMARY")
    print("="*85)
    for idx, student in enumerate(student_list, start=1):
        print(f"[{idx}] ", end="")
        student.displayDetails()
    print("="*85)


if __name__ == "__main__":
    #Store student objects in a list
    students = []
    
    print("=== Student Data Entry Portal ===")
    print("Please enter information for at least 3 students.\n")
    
    count = 0
    while count < 3:
        print(f"--- Enter Details for Student {count + 1} ---")
        name = input("Enter student name: ")
        reg_number = input("Enter registration number: ")
        course = input("Enter course: ")
        
       
        try:
            mark_input = input("Enter mark (0 - 100): ")
            mark = float(mark_input)
    
            if not (0 <= mark <= 100):
                raise ValueError("Mark out of bounds (must be between 0 and 100).")

            new_student = Student(name, reg_number, course, mark)
            students.append(new_student)
            count += 1
            print("Student added successfully!\n")
            
        except ValueError as err:
            print(f"❌ Invalid mark entered: {err}. Please enter a valid numeric mark.\n")

    displayStudents(students)

    file = open("students.txt", "w")
    
    file.write("--- Official University Student Records ---\n")
    for student in students:
        grade = student.calculateGrade()
        record_line = f"Name: {student.name} | Reg No: {student.reg_number} | Course: {student.course} | Mark: {student.mark} | Grade: {grade}\n"
        file.write(record_line)

    file.close()
    print("\nSuccess! All student records have been saved to 'students.txt' and the file has been securely closed.")
