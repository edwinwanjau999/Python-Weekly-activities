#Create a list named marks containing five subject marks
marks = [85, 92, 78, 90, 88]

#Display all the marks
print("Original Marks:")
print(marks)

#Calculate and display the total marks using sum()
total_marks = sum(marks)
print("\nTotal Marks:", total_marks)

#Calculate and display the average mark
average_mark = total_marks / len(marks)
print("Average Mark:", average_mark)

#Display the highest mark using max()
highest_mark = max(marks)
print("Highest Mark:", highest_mark)

#Display the lowest mark using min()
lowest_mark = min(marks)
print("Lowest Mark:", lowest_mark)


marks[2] = 95
print("\nUpdated Marks (after modifying the third subject):")
print(marks)
