# i. Create a parent class named Employee
class Employee:
    def __init__(self, name, emp_id):
        # Parent attributes: Employee name and Employee ID
        self.name = name
        self.emp_id = emp_id

    # ii. Include a method named displayEmployee() to display employee details
    def displayEmployee(self):
        print(f"Employee Name : {self.name}")
        print(f"Employee ID   : {self.emp_id}")


# iii. Create a child class named Lecturer that inherits from Employee
class Lecturer(Employee):
    def __init__(self, name, emp_id, teaching_subject):
        # Call the parent class's constructor using super() to initialize inherited attributes
        super().__init__(name, emp_id)
        
        # iv. Add the teaching subject attribute to the Lecturer class
        self.teaching_subject = teaching_subject

    # v. Include a method named displayLecturer() to display name, ID, and teaching subject
    def displayLecturer(self):
        print("\n--- Lecturer Profile Report ---")
        # Reuse parent display method
        self.displayEmployee()
        print(f"Teaching Subject: {self.teaching_subject}")


# vi. In the main section
if __name__ == "__main__":
    # Create a Lecturer object, assigning employee details and teaching subject
    lecturer1 = Lecturer(
        name="Dr. James Mwangi", 
        emp_id="EMP-4052", 
        teaching_subject="Advanced Object-Oriented Programming"
    )

    # Display all information by calling displayLecturer()
    lecturer1.displayLecturer()
