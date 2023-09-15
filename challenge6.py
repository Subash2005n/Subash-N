def sort_students(students):
    return sorted(students, key=lambda student: student.cgpa, reverse=True)
class Student:
    def __init__(self, name, roll_number, cgpa):
        self.name = name
        self.roll_number = roll_number
        self.cgpa = cgpa

students = [
    Student("mani", "1", 3.5),
    Student("monish", "2", 3.7),
    Student("naveen", "3", 3.5),
    Student("nishanth", "4", 3.8),
]

sorted_students = sort_students(students)

for student in sorted_students:
    print(student.name, student.roll_number, student.cgpa)