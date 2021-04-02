class Class:
    __students_count = 22
    def __init__(self, name):
        self.name = name
        self.students = []
        self.grades = []
    def add_student(self, name, grade):
        if Class.__students_count > 0:
            self.students.append(name)
            self.grades.append(grade)
            Class.__students_count -= 1
    def get_average_grade(self):
        self.average_grade = f"{(sum(self.grades)/(22-(Class.__students_count))):.2f}"
        return self.average_grade
    def __repr__(self):
        studentss = ", ".join(self.students)
        return f"The students in {self.name}: {studentss}. Average grade: {(sum(self.grades)/(22-(Class.__students_count))):.2f}"
a_class = Class("11B")
a_class.add_student("Peter", 4.80)
a_class.add_student("George", 6.00)
a_class.add_student("Amy", 3.50)
print(a_class)