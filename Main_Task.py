class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer,
                      Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Error'

    def av_rate_lec(self):
        for key, value in Lecturer.grades:
            print(value)
        return "Grades"

    def __str__(self):
        Student.av_rate_lec(self)
        return f"Name: {self.name}\nSurname: {self.surname}"


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.courses_in_progress = []
        self.finished_courses = []
        self.grades = {}

    def __str__(self):
        some_student = (f"Name: {self.name}"
                        f"\nSurname: {self.surname}"
                        f"\nAverage assessment for lecturers:{self.grades}"
                        f"\nCourses: {','.join(self.courses_in_progress)}"
                        f"\nCourses studied: {','.join(self.finished_courses)} ")
        return some_student


class Lecturer(Mentor):
    grades = {}


class Reviewer(Mentor):
    def rate_homework(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Error'


student_1 = Student('Ivan', 'Moshnov', 'M')
student_1.courses_in_progress += ['Python']
student_1.courses_in_progress += ['GO']
student_1.courses_in_progress += ['Java']

reviewer_1 = Reviewer('Gleb', 'Petrovykh')
reviewer_1.courses_attached += ['Python']
reviewer_1.courses_attached += ['Java']
reviewer_1.courses_attached += ['GO']
print("\n")
print(f'Reviewer: {reviewer_1.name} {reviewer_1.surname}\nLead Courses: {" ".join(reviewer_1.courses_attached)}\n')

reviewer_1.rate_homework(student_1, 'Python', 10)
reviewer_1.rate_homework(student_1, 'Java', 10)
reviewer_1.rate_homework(student_1, 'GO', 8)
print(f'Rates: {student_1.name} {student_1.surname}\n{student_1.grades}')
print("\n")

lecturer_1 = Lecturer('Mark', 'Liberman')
lecturer_1.courses_attached += ['Python']
lecturer_1.courses_attached += ['Java']
lecturer_1.courses_attached += ['GO']

student_1.rate_lecturer(lecturer_1, 'Python', 10)
student_1.rate_lecturer(lecturer_1, 'Java', 7)
student_1.rate_lecturer(lecturer_1, 'GO', 3)
print(f'Rate of Lecturers: {lecturer_1.name} {lecturer_1.surname}\n{lecturer_1.grades}')
print("\n")

print(student_1)

print(reviewer_1)

print(lecturer_1)
