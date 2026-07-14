# Task 1 & 4
class Student:
    def __init__(self, name, age, marks):
        self.name = name
        self.age = age
        self.marks = marks

    def __str__(self):
        return f"{self.name} {self.age} {self.marks}"

    def score(self):
        if self.marks > 70:
            print("Pass")
        else:
            print("Fail")

student1 = Student("Ali", 20, 90)

print(student1)
student1.score()