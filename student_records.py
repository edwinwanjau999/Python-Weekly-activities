#Open a file named students.txt in write mode ('w')
file = open("students.txt", "w")

#Write information for at least three students using print(..., file=f)
print("Student Name: Alice Smith | Reg No: S01/1001/2026 | Course: Computer Science | Mark: 85", file=file)
print("Student Name: Bob Jones | Reg No: S01/1002/2026 | Course: Information Technology | Mark: 78", file=file)
print("Student Name: Clara Mwangi | Reg No: S01/1003/2026 | Course: Software Engineering | Mark: 92", file=file)

#Close the file using close()
file.close()

print("Success! Student records have been written to 'students.txt'.")
