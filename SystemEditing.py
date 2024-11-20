import json
import logging

logging.basicConfig(level=logging.INFO)

class StudentSystem:
    def __init__(self):
        self.students = {}  # Dictionary to store student data: {student_id: {'name': name, 'grades': {course: grade}}}
        self.courses = {}
        self.users = {"admin": "password"}  # Example user
        logging.info("StudentSystem initialized")

    def authenticate(self, username, password):
        return self.users.get(username) == password

    def add_student(self, student_id, name):
        if student_id not in self.students:
            self.students[student_id] = {'name': name, 'grades': {}}
            logging.info(f"Added student: {student_id} - {name}")
            return True
        logging.warning(f"Student {student_id} already exists")
        return False

    def add_course(self, course_id, course_name):
        if course_id not in self.courses:
            self.courses[course_id] = {'name': course_name, 'students': {}}
            logging.info(f"Added course: {course_id} - {course_name}")
            return True
        logging.warning(f"Course {course_id} already exists")
        return False

    def remove_course(self, course_id):
        if course_id in self.courses:
            del self.courses[course_id]
            logging.info(f"Removed course: {course_id}")
            return True
        logging.warning(f"Course {course_id} does not exist")
        return False

    def add_grade(self, student_id, course, grade):
        if student_id in self.students:
            self.students[student_id]['grades'][course] = grade
            logging.info(f"Added grade for student {student_id} in course {course}: {grade}")
            return True
        logging.warning(f"Student {student_id} does not exist")
        return False

    def edit_grade(self, student_id, course, new_grade):
        """
        Edit a student's grade for a specific course
        Returns True if successful, False if student or course not found
        """
        if student_id in self.students:
            if course in self.students[student_id]['grades']:
                self.students[student_id]['grades'][course] = new_grade
                logging.info(f"Edited grade for student {student_id} in course {course}: {new_grade}")
                return True
        logging.warning(f"Student {student_id} or course {course} does not exist")
        return False

    def get_student_grades(self, student_id):
        if student_id in self.students:
            logging.info(f"Retrieved grades for student {student_id}")
            return self.students[student_id]['grades']
        logging.warning(f"Student {student_id} does not exist")
        return None

    def save_to_file(self, filename):
        with open(filename, 'w') as file:
            json.dump(self.students, file)
        logging.info(f"Saved student data to {filename}")

    def load_from_file(self, filename):
        with open(filename, 'r') as file:
            self.students = json.load(file)
        logging.info(f"Loaded student data from {filename}")

    def search_student(self, name):
        return {sid: info for sid, info in self.students.items() if name.lower() in info['name'].lower()}

    def search_course(self, course_name):
        return {cid: info for cid, info in self.courses.items() if course_name.lower() in info['name'].lower()}

    def enroll_student_in_course(self, student_id, course_id):
        if student_id in self.students and course_id in self.courses:
            self.courses[course_id]['students'][student_id] = self.students[student_id]
            logging.info(f"Enrolled student {student_id} in course {course_id}")
            return True
        logging.warning(f"Enrollment failed for student {student_id} in course {course_id}")
        return False

    def unenroll_student_from_course(self, student_id, course_id):
        if course_id in self.courses and student_id in self.courses[course_id]['students']:
            del self.courses[course_id]['students'][student_id]
            logging.info(f"Unenrolled student {student_id} from course {course_id}")
            return True
        logging.warning(f"Unenrollment failed for student {student_id} from course {course_id}")
        return False

    def generate_report(self):
        report = "Student Report\n"
        for student_id, student_info in self.students.items():
            report += f"ID: {student_id}, Name: {student_info['name']}\n"
            for course_id, grade in student_info['grades'].items():
                report += f"  Course: {course_id}, Grade: {grade}\n"
        return report

# Example usage:
if __name__ == "__main__":
    system = StudentSystem()
    
    # Add a student
    system.add_student("001", "John Doe")
    
    # Add initial grade
    system.add_grade("001", "Math", 85)
    
    # Edit the grade
    system.edit_grade("001", "Math", 90)
    
    # View updated grades
    print(system.get_student_grades("001"))