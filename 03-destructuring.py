
x = 4, 5
x = (4, 5)
print(x)

student_attendance = {"Rolf": 96, "Bob": 80, "Anne": 100}

# print(student_attendance.items())
for student, attendance in student_attendance.items():
    print(f"{student}: {attendance}")

x = [(1, 2), (3, 4), (5, 6)]
for a, b in x:
    print(a)

*head, tail = [1, 2, 3, 4, 5, 6]
print(head)
print(tail)

a, b = [1, 2]
print(a)
print(b)
