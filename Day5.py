class Student:
    def __init__(self, name: str, marks: list):
        self.name = name
        self.marks = marks

    def average(self) -> float:
        if len(self.marks) == 0:
            return 0
        return sum(self.marks) / len(self.marks)
s1 = Student("Lakshya", [85, 90, 78, 92, 88])
print("Name:", s1.name)
print("Marks:", s1.marks)
print("Average Marks:", s1.average())
