
students = {
    "Aman": 85,
    "Lakshya": 92,
    "Riya": 76,
    "Neha": 89,
    "Arjun": 95
}
top_student = max(students, key=students.get)
print("Top student:", top_student)
print("Marks:", students[top_student])
