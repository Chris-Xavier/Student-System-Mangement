import unittest
from StudentSystem import Student, Course
from SystemEditing import StudentSystem

class TestStudentSystem(unittest.TestCase):
    def test_add_student(self):
        system = StudentSystem()
        self.assertTrue(system.add_student("001", "John Doe"))
        self.assertFalse(system.add_student("001", "Jane Doe"))

    def test_add_grade(self):
        system = StudentSystem()
        system.add_student("001", "John Doe")
        self.assertTrue(system.add_grade("001", "Math", 85))
        self.assertFalse(system.add_grade("002", "Math", 85))

    def test_edit_grade(self):
        system = StudentSystem()
        system.add_student("001", "John Doe")
        system.add_grade("001", "Math", 85)
        self.assertTrue(system.edit_grade("001", "Math", 90))
        self.assertFalse(system.edit_grade("001", "Science", 90))

if __name__ == '__main__':
    unittest.main()