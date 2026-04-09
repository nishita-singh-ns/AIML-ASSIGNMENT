### CODE CELL ###
students = {}

# Taking input for 5 students
for i in range(5):
    name = input("Enter student name: ")
    marks = float(input("Enter marks: "))
    students[name] = marks

# Finding topper
topper = max(students, key=students.get)
highest_marks = students[topper]

# Calculating class average
total = sum(students.values())
average = total / 5

print("\n--- Results ---")
print("Topper:", topper, "with", highest_marks, "marks")
print("Class Average:", average)

# Assigning Grades
print("\nGrades:")
for name, marks in students.items():
    if marks >= 90:
        grade = "A"
    elif marks >= 75:
        grade = "B"
    elif marks >= 50:
        grade = "C"
    else:
        grade = "Fail"

    print(name, ":", grade)

### CODE CELL ###


