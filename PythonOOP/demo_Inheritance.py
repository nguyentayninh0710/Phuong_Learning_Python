from __future__ import annotations
from typing import List, Optional

class Person: 
    def __init__(self, createName: str, createAge: int):
        self.name = createName
        self.age = createAge
    def introduce(self) -> str:
        return f"I am {self.name}, {self.age} years old"
    
class Student(Person):
    def __init__(self, createName, createAge, sdt_id: str):
        super().__init__(createName, createAge)
        self.student_id = sdt_id
    def introduce(self):
        return f"Student {self.name}, (ID: {self.student_id}, age: {self.age})"

def find_student_by_id(students: List[Student], student_id: str) -> Optional[Student]:
    for st in students:
        if st.student_id == student_id:
            return st
        return None
        
def demo_Inheritance() -> None:
    studentList: List[Student] = [
        Student("Phuong", 18, "S001"),
        Student("An", 17, "S002"),
        Student("Vu", 17, "S003")
    ]

    for st in studentList:
        print(st.introduce())

    std = find_student_by_id(studentList, "S001")
    print("Search student S001", std.introduce())