# This program reads student names from a file, assigns random grades, stores them in
# a dictionary, writes the results to a new file, and displays summary statistics.

# Import the random module
import random

# STEP 1: Read names from the file
# Open the file in read mode
with open("names_list.txt", "r") as file:
    # Read entire file as one string
    names_data = file.read()

# Split the names by commas to create a list
names_list = names_data.split(",")

# Remove extra spaces from each name
cleaned_names = []
for name in names_list:
    cleaned_names.append(name.strip())

# STEP 2: Generate random grades (50–100) and store in dictionary
grades_dict = {}

for name in cleaned_names:
    # Generate random grade between 50 and 100
    grade = random.randint(50, 100)
    # Store in dictionary (name = key, grade = value)
    grades_dict[name] = grade

# STEP 3: Write dictionary data to new file
with open("names_and_grades.txt", "w") as new_file:
    for name, grade in grades_dict.items():
        # format: Student name received a grade of grade
        new_file.write(f"{name} received a grade of {grade}\n")

# STEP 4: Find top grade
top_grade = max(grades_dict.values())

# Get all students who earned the top grade
top_students = []
for name, grade in grades_dict.items():
    if grade == top_grade:
        top_students.append(name)

# STEP 5: Find bottom grade
bottom_grade = min(grades_dict.values())

# Get all students who earned the bottom grade
bottom_students = []
for name, grade in grades_dict.items():
    if grade == bottom_grade:
        bottom_students.append(name)

# STEP 6: Calculate average grade
total = sum(grades_dict.values())
average = total / len(grades_dict)

# STEP 7: Print output

# Print top grade student(s)
for student in top_students:
    print(f"The student with the top grade of {top_grade} is {student}")
    print()

# Print bottom grade student(s)
for student in bottom_students:
    print(f"The student with the bottom grade of {bottom_grade} is {student}")
    print()

# Print average with one decimal precision
print(f"The average grade is {average:.1f}")