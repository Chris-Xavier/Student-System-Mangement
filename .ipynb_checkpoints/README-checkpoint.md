# Student-System-Management

## Overview
The Student System Management program is a comprehensive tool designed to manage students and courses efficiently. It provides functionalities to add, edit, and remove students and courses, enroll and unenroll students in courses, manage grades, and search for students and courses. The system also includes a command-line interface (CLI) for easy interaction and supports data persistence.

## Features
- Add, edit, and remove students
- Add, edit, and remove courses
- Enroll and unenroll students in courses
- Add and edit grades
- Search for students and courses
- Save and load data from a file
- Command-line interface (CLI)
- Generate student reports

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/student-system-management.git
    cd student-system-management
    ```

2. Ensure you have Python installed (version 3.6 or higher).

3. Install any required dependencies (if applicable).

## Usage

### Command-Line Interface (CLI) Usage

#### Adding a Student
To add a new student, use the `--add-student` option followed by the student ID and name:
```sh
python [CommandLineInterface.py](http://_vscodecontentref_/0) --add-student 001 "John Doe"

Adding a Course
To add a new course, use the --add-course option followed by the course ID and name:

python [CommandLineInterface.py](http://_vscodecontentref_/1) --add-course 101 "Math"

Enrolling a Student in a Course
To enroll a student in a course, use the --enroll option followed by the student ID and course ID:

python [CommandLineInterface.py](http://_vscodecontentref_/2) --enroll 001 101

Unenrolling a Student from a Course
To unenroll a student from a course, use the --unenroll option followed by the student ID and course ID:

python [CommandLineInterface.py](http://_vscodecontentref_/3) --unenroll 001 101

Searching for a Student
To search for a student by name, use the --search-student option followed by the student's name:

python [CommandLineInterface.py](http://_vscodecontentref_/4) --search-student "John"

Searching for a Course
To search for a course by name, use the --search-course option followed by the course name:

python [CommandLineInterface.py](http://_vscodecontentref_/5) --search-course "Math"

Generating a Student Report
To generate a report of all students and their enrolled courses, use the --report option:

python [CommandLineInterface.py](http://_vscodecontentref_/6) --report

Running Tests
To run the unit tests, use the following command:

python -m unittest discover

```
Contributing
Contributions are welcome! Please fork the repository and submit a pull request with your changes. Ensure your code follows best practices and includes appropriate tests.

License
This project is licensed under the MIT License. See the LICENSE file for details.

Contact
For any questions or suggestions, please contact chrisxavier1225@gmail.com