#Use a try block to open employees.txt in read mode ('r')
try:
    file = open("employees.txt", "r")
    
    #Read and display the contents of the file
    file_contents = file.read()
    print("--- Employee Information ---")
    print(file_contents)
    
    # Close the file after successful reading
    file.close()

#Use an except FileNotFoundError block to handle a missing file
except FileNotFoundError:
    # Display the required error message when the file does not exist
    print("The employee file was not found.")

# Use a finally block to display the completion message regardless of whether the file was found or not
finally:
    print("File processing completed.")
