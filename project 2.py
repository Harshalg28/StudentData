    #SOURAV
class Student:
    def __init__(self, roll_no, name, age, department):
        self.roll_no = roll_no
        self.name = name
        self.age = age
        self.department = department

class StudentSystem:
    def __init__(self):
        self.students = []

    def add_student(self, roll_no, name, age, department):
        student = Student(roll_no, name, age, department)
        self.students.append(student)
        print(f"Student {name} added successfully!")

    def view_students(self):
        if not self.students:
            print("No students in the system.")
        else:
            print("Student Records:")
            for student in self.students:
                print(f"Roll No: {student.roll_no}, Name: {student.name}, Age: {student.age}, Department: {student.department}")

    def search_student(self, roll_no):
        for student in self.students:
            if student.roll_no == roll_no:
                print(f"Student found - Roll No: {student.roll_no}, Name: {student.name}, Age: {student.age}, Department: {student.department}")
                return
        print(f"Student with Roll No {roll_no} not found in the system.")

def main():
    student_system = StudentSystem()

    while True:
        print("\nStudent Information System")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Quit")

        choice = input("Enter your choice: ")

        if choice == '1':
            roll_no = input("Enter Roll No: ")
            name = input("Enter Name: ")
            age = input("Enter Age: ")
            department = input("Enter Department: ")
            student_system.add_student(roll_no, name, age, department)
        elif choice == '2':
            student_system.view_students()
        elif choice == '3':
            roll_no = input("Enter Roll No to search: ")
            student_system.search_student(roll_no)
        elif choice == '4':
            print("Exiting Student Information System. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
