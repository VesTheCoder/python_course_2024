class Person:
    def __init__(self, first_name: str, last_name: str):
        self.first_name = first_name.strip().title()
        self.last_name = last_name.strip().title()

    def __str__(self):
        return f"{self.first_name} {self.last_name[0]}."
   
class Students(Person):
    def __init__(self, first_name: str, last_name: str, inGroup: str):
        super().__init__(first_name, last_name)
        self.inGroup = inGroup
        
    def __str__(self):
        return f"{self.first_name} {self.last_name[0]}, learns in {self.inGroup}"
    
class Teacher(Person):
    def __init__(self, first_name: str, last_name: str, discipline: str):
        super().__init__(first_name, last_name)
        self.discipline = discipline

    def __str__(self):
        return f"{self.first_name} {self.last_name}, teaches {self.discipline}"

class Group:
    def __init__(self, title: str, teacher: Teacher, start_date: str):
        self.__title = title
        self.__teacher = teacher
        self.start_date = start_date
        self.__students = []

    def add_student(self, student: Students):
        if isinstance(student, Students) and student not in self.__students:
            self.__students.append(student)

    def __str__(self):
        return f"Group {self.__title}. \nTeacher: {self.__teacher} \nStudents: \n{"\n".join(map(str, self.__students))}"
    
teacher_1 = Teacher("Oleh", "Tymchuk", "Python")
group_1 = Group("Python Pro", teacher_1, "01.08.2024")
student_1 = Students("Vlad", "Y", "Python Pro")
student_2 = Students("Rodion", "D", "Python Pro")
student_3 = Students("Igor", "K", "Python Pro")

group_1.add_student(student_1)
group_1.add_student(student_2)
group_1.add_student(student_3)

print(group_1)