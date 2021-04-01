students = {}
n = int(input())
for i in range(n):
    name = input()
    grade = float(input())

    if name not in students:
        students[name] = []
    students[name].append(grade)
filtered_student_averages = {}
for student in students:
    average = sum(students[student])/len(students[student])
    if average >= 4.5:
        filtered_student_averages[student] = average
sorted_students = sorted(filtered_student_averages.items(),key= lambda kvp:-kvp[1])
for student, average in sorted_students:
    print(f"{student} -> {average:.2f}")

