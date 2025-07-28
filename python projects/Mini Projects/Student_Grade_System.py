# #Initial dict
# student_grades = {}
#
# #Add a new student
# def add_student (name, grade):
#     student_grades[name] = grade
#     print(f"Added {name} with a{ grade}")
#
# #Update student
# def update_student(name, grade):
#     if name in student_grades:
#         student_grades[name] = grade
#         print(f" {name} with marks are updated {grade}")
#
#     else:
#         print(f"{name} is not found!")
#
# # Delete a student
# def delete_function(name):
#     if name in student_grades:
#         del student_grades[name]
#         print(f"{name} has been deleted")
#
#     else:
#         print(f"{name} is not found!")
#
# # view all students
# def view_all():
#     if student_grades:
#         for name, grade in student_grades.items():
#             print(f"{name} : {grade}")
#
#     else:
#         print("No students found..")
#
#
#
# def main():
#     while True:
#
#         print('\n Students Grade Management System')
#         print('1. Add Student')
#         print('2. Update Student')
#         print('3. Delete Student')
#         print('4. View Student')
#         print('5. Exit')
#
#
#         choice = int(input('Enter your choice'))
#         if choice==1:
#             name = input('Enter student name=')
#             grade = int(input('Enter student grade='))
#             add_student(name, grade)
#
#         elif choice == 2:
#             name = input('Enter student name=')
#             grade = int(input('Enter student grade='))
#             update_student(name, grade)
#
#         elif choice==3:
#             name= input('Enter student name=')
#             delete_function(name)
#
#         elif choice ==4:
#             view_all()
#
#         elif choice ==5:
#             print("closing the program")
#             break
#
#         else:
#             print('Invalid input')
#

# import json
#
# student_grades = {}
#
# def load_grades():
#     try:
#         with open("grades.json") as f:
#             return json.load(f)
#     except FileNotFoundError:
#         return {}
#
# def save_grades():
#     with open("grades.json", "w") as f:
#         json.dump(student_grades, f)
#
# def set_grade(name, grade):
#     student_grades[name] = grade
#     print(f"Set {name}'s grade to {grade}.")
#
# def delete_student(name):
#     if name in student_grades:
#         del student_grades[name]
#         print(f"{name} has been deleted.")
#     else:
#         print(f"{name} not found.")
#
# def view_student(name=None):
#     if name:
#         grade = student_grades.get(name)
#         print(f"{name} : {grade}" if grade is not None else f"{name} not found.")
#     else:
#         if student_grades:
#             for n, g in student_grades.items():
#                 print(f"{n} : {g}")
#         else:
#             print("No students found.")
#
# def main():
#     global student_grades
#     student_grades = load_grades()
#
#     while True:
#         print("""
#         🧑‍🎓 Student Grade Management System
#         1. Add / Update Student Grade
#         2. Delete Student
#         3. View All Students
#         4. View Single Student
#         5. Exit
#         """)
#         try:
#             choice = int(input("Enter choice: "))
#         except ValueError:
#             print("Enter a number from 1 to 5.")
#             continue
#
#         if choice == 1:
#             name = input("Student name: ").strip()
#             try:
#                 grade = int(input("Grade: "))
#             except ValueError:
#                 print("Grade must be a number.")
#                 continue
#             set_grade(name, grade)
#
#         elif choice == 2:
#             delete_student(input("Student name: ").strip())
#
#         elif choice == 3:
#             view_student()
#
#         elif choice == 4:
#             view_student(input("Student name: ").strip())
#
#         elif choice == 5:
#             save_grades()
#             print("Goodbye!")
#             break
#
#         else:
#             print("Invalid choice. Please enter 1–5.")



import os
import json

student_grades = {}

def load_grades():
    try:
        with open("grades.json") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def save_grades():
    with open("grades.json", "w") as f:
        json.dump(student_grades, f, indent=2)

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def pause():
    input("\nPress Enter to return to the menu...")

def set_grade(name, grade):
    student_grades[name] = grade
    print(f"✅ Set {name}'s grade to {grade}.")

def delete_student(name):
    if name in student_grades:
        del student_grades[name]
        print(f"🗑️  {name} has been deleted.")
    else:
        print(f"❗ {name} not found.")

def view_student(name=None):
    if name:
        grade = student_grades.get(name)
        if grade is not None:
            print(f"{name}: {grade}")
        else:
            print(f"❗ {name} not found.")
    else:
        if student_grades:
            print("👥 All Students:")
            for n, g in student_grades.items():
                print(f"  • {n}: {g}")
        else:
            print("ℹ️  No students found.")

def main():
    global student_grades
    student_grades = load_grades()

    while True:
        clear_screen()
        print("🧑‍🎓 Student Grade Management System")
        print("-------------------------------")
        print("1. Add / Update Student Grade")
        print("2. Delete Student")
        print("3. View All Students")
        print("4. View Single Student")
        print("5. Exit")

        try:
            choice = int(input("Enter choice (1–5): "))
        except ValueError:
            print("❗ Enter a valid number from 1 to 5.")
            pause()
            continue

        if choice == 1:
            name = input("Student name: ").strip()
            if not name:
                print("❗ Name cannot be empty.")
                pause()
                continue

            try:
                grade = int(input("Grade (0–100): "))
                if grade < 0 or grade > 100:
                    raise ValueError()
            except ValueError:
                print("❗ Grade must be an integer between 0 and 100.")
                pause()
                continue

            set_grade(name, grade)
            pause()

        elif choice == 2:
            name = input("Student name to delete: ").strip()
            delete_student(name)
            pause()

        elif choice == 3:
            view_student()
            pause()

        elif choice == 4:
            name = input("Student name to view: ").strip()
            view_student(name)
            pause()

        elif choice == 5:
            save_grades()
            print("✅ Grades saved. Goodbye!")
            break

        else:
            print("❗ Invalid option. Please enter 1–5.")
            pause()

if __name__ == "__main__":
    main()


