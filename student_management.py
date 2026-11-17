#Create a class named Student with attributes
class Student:
    def __init__(self):
        # Initializing attributes to empty/default values
        self.student_name = ""
        self.registration_number = ""
        self.course = ""
        self.mark = 0.0

    #Include the specified methods
    def setStudentDetails(self, name, reg_number, course, mark):
        """To assign student information."""
        self.student_name = name
        self.registration_number = reg_number
        self.course = course
        self.mark = mark

    def calculateGrade(self):
        """To calculate the grade using the university criteria."""
        if 70 <= self.mark <= 100:
            return "A"
        elif 60 <= self.mark <= 69:
            return "B"
        elif 50 <= self.mark <= 59:
            return "C"
        elif 40 <= self.mark <= 49:
            return "D"
        else:
            return "F"  # Below 40

    def displayStudentDetails(self):
        """To display the student's information and grade."""
        grade = self.calculateGrade()
        print("\n--- Student Information Report ---")
        print(f"Student Name       : {self.student_name}")
        print(f"Registration Number: {self.registration_number}")
        print(f"Course             : {self.course}")
        print(f"Mark               : {self.mark}")
        print(f"Grade              : {grade}")


#In the main section
if __name__ == "__main__":
    # Create a Student object
    student1 = Student()

    # Set the student's details
    student1.setStudentDetails(
        name="Brian Kiprop",
        reg_number="S01/98765/2026",
        course="Bachelor of Business Information Technology",
        mark=76
    )

    # Display the student details and grade (calculateGrade is automatically invoked inside displayStudentDetails)
    student1.displayStudentDetails()
