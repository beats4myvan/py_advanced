student_range = int(input())

students = {}
for _ in range(student_range):
    student = input()
    name, grades = student.split(" ")
    if name not in students:
        students[name] = []
        students[name].append(float(grades))
    else:
        students[name].append(float(grades))
for (x, y) in students.items():
    avg_grade = sum(y) / len(y)
    grade_string = ' '.join(f'{grade:.2f}' for grade in y)
    print(f'{x} -> {grade_string} (avg: {avg_grade:.2f})')
