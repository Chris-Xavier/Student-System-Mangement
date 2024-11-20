import argparse
from SystemEditing import StudentSystem

def main():
    parser = argparse.ArgumentParser(description="Student System Management CLI")
    parser.add_argument("--add-student", nargs=2, metavar=('ID', 'NAME'), help="Add a new student")
    parser.add_argument("--add-course", nargs=2, metavar=('ID', 'NAME'), help="Add a new course")
    parser.add_argument("--enroll", nargs=2, metavar=('STUDENT_ID', 'COURSE_ID'), help="Enroll a student in a course")
    parser.add_argument("--unenroll", nargs=2, metavar=('STUDENT_ID', 'COURSE_ID'), help="Unenroll a student from a course")
    parser.add_argument("--search-student", metavar='NAME', help="Search for a student by name")
    parser.add_argument("--search-course", metavar='NAME', help="Search for a course by name")
    parser.add_argument("--report", action='store_true', help="Generate student report")
    args = parser.parse_args()

    system = StudentSystem()

    if args.add_student:
        system.add_student(*args.add_student)
    if args.add_course:
        system.add_course(*args.add_course)
    if args.enroll:
        system.enroll_student_in_course(*args.enroll)
    if args.unenroll:
        system.unenroll_student_from_course(*args.unenroll)
    if args.search_student:
        students = system.search_student(args.search_student)
        for sid, info in students.items():
            print(f"ID: {sid}, Name: {info['name']}")
    if args.search_course:
        courses = system.search_course(args.search_course)
        for cid, info in courses.items():
            print(f"ID: {cid}, Name: {info['name']}")
    if args.report:
        print(system.generate_report())

if __name__ == "__main__":
    main()