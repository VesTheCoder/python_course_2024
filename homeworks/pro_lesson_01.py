class Student:
    def __init__(self, first_name, last_name, date_of_birth=None):
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Group:

    def __init__(self, title):
        self.title = title
        self.__students = []

    def add_student(self, student: Student):
        if isinstance(student, Student) and student not in self.__students:
            self.__students.append(student)

    def __str__(self):
        return '\n'.join(map(str, self.__students))


gr_1 = Group('Group 1')
while answer := input('Do you want to add a student? (y/n) ').lower().strip() == 'y':
    first_name = input('Enter first name: ').strip().title()
    last_name = input('Enter last name: ').strip().title()
    st = Student(first_name, last_name)
    gr_1.add_student(st)

print(gr_1)