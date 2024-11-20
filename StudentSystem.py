class Student:
    def __init__(self, name, student_id):
        if not name or not student_id:
            raise ValueError("Name and student ID cannot be empty")
        if not isinstance(student_id, str) or not student_id.isdigit():
            raise ValueError("Student ID must be a numeric string")
        self.name = name
        self.student_id = student_id
        self.courses = {}

    def enroll(self, course):
        if not isinstance(course, Course):
            raise TypeError("Invalid course")
        if course.course_id not in self.courses:
            self.courses[course.course_id] = course
            course.add_student(self)

    def add_grade(self, course, grade):
        if course.course_id in self.courses:
            self.courses[course.course_id].add_grade(self, grade)

    def get_grades(self):
        return {course.course_name: course.get_grade(self) for course in self.courses.values()}

class Course:
    def __init__(self, course_name, course_id):
        self.course_name = course_name
        self.course_id = course_id
        self.students = {}
        self.grades = {}

    def add_student(self, student):
        if student.student_id not in self.students:
            self.students[student.student_id] = student

    def add_grade(self, student, grade):
        if student.student_id in self.students:
            self.grades[student.student_id] = grade

    def get_grade(self, student):
        return self.grades.get(student.student_id, None)

# Example usage
student1 = Student("Alice", "1")
student2 = Student("Bob", "2")
course1 = Course("Math", 101)
course2 = Course("Science", 102)

student1.enroll(course1)
student2.enroll(course2)

student1.add_grade(course1, 'A')
student2.add_grade(course2, 'B')

print(student1.get_grades())  # Output: {'Math': 'A'}
print(student2.get_grades())  # Output: {'Science': 'B'}