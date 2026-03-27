students = {
    "Amit": 85,
    "Rahul": 92,
    "Sneha": 78,
    "Priya": 88,
    "Arjun": 95
}

# Topper
topper = max(students, key=students.get)

# Average
average = sum(students.values()) / len(students)

print("Topper:", topper)
print("Class Average:", average)

# Assign grades
for student, marks in students.items():

    if marks >= 90:
        grade = "A"
    elif marks >= 80:
        grade = "B"
    elif marks >= 70:
        grade = "C"
    else:
        grade = "D"

    print(student, "Marks:", marks, "Grade:", grade)