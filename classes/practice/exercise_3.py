class Student:
    def __init__(self, grades):
        self.grades = grades

    def add_grade(self, grade):
        self.grades.append(grade)
        print(f"A grade of {grade} was added for this student.")

    def average(self):
        print(f"The average of the grades is {sum(self.grades) / len(self.grades):.2f}.")

student1 = Student([90, 100, 75])
student1.add_grade(100)
student1.average()