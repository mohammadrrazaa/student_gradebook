import csv
from statistics import mean

class Student:
    def __init__(self, name):
        self.name = name
        self.grades = []

    def add_grade(self, grade: float):
        self.grades.append(grade)

    def average(self):
        return mean(self.grades) if self.grades else 0

    def gpa(self):
        # Simple GPA scale (A=4, B=3, C=2, D=1, F=0)
        avg = self.average()
        if avg >= 90: return 4.0
        elif avg >= 80: return 3.0
        elif avg >= 70: return 2.0
        elif avg >= 60: return 1.0
        else: return 0.0

    def __str__(self):
        return f"{self.name} | Avg: {self.average():.2f} | GPA: {self.gpa():.2f}"


class Gradebook:
    def __init__(self, filename="gradebook.csv"):
        self.students = {}
        self.filename = filename
        self.load()

    def add_student(self, name):
        if name not in self.students:
            self.students[name] = Student(name)

    def add_grade(self, name, grade):
        self.add_student(name)
        self.students[name].add_grade(grade)
        self.save()

    def display(self):
        print("\n--- Gradebook ---")
        for student in self.students.values():
            print(student)

    def save(self):
        with open(self.filename, "w", newline="") as f:
            writer = csv.writer(f)
            for student in self.students.values():
                writer.writerow([student.name] + student.grades)

    def load(self):
        try:
            with open(self.filename, "r") as f:
                reader = csv.reader(f)
                for row in reader:
                    name, *grades = row
                    self.students[name] = Student(name)
                    for g in grades:
                        self.students[name].add_grade(float(g))
        except FileNotFoundError:
            pass  # start fresh


def main():
    gb = Gradebook()
    while True:
        print("\n1. Add Student\n2. Add Grade\n3. Show Gradebook\n4. Exit")
        choice = input("Choose: ")
        if choice == "1":
            name = input("Student name: ")
            gb.add_student(name)
        elif choice == "2":
            name = input("Student name: ")
            grade = float(input("Grade (0-100): "))
            gb.add_grade(name, grade)
        elif choice == "3":
            gb.display()
        elif choice == "4":
            break


if __name__ == "__main__":
    main()
