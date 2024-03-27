import numpy as np
import subjects
import student


# generate students list and displays table
def generate_students_table(n):
    students = []
    for _ in range(n):
        students.append(student.Student())
    student_grades = []

    for stu in students:
        student_grades.append([stu.get_full_name()] + stu.get_grades())

    subject_names = np.array(subjects.SUBJECTS.list_names())

    student_grades = np.array(student_grades, dtype=object)
    subject_names = subject_names.reshape((1, 11))
    student_table = np.vstack((subject_names, student_grades))

    for row in student_table:
        print(' '.join([str(elem).ljust(20) for elem in row]))

    return students, student_table


# calculates average grades of students
def calculate_average_grades(students):
    average_grades = np.array([np.mean(stu.get_grades()) for stu in students])
    return average_grades


# displays student with highest average grade
def display_highest_average(students):
    average_grades = calculate_average_grades(students)
    highest_average_index = np.argmax(average_grades)
    highest_average_student = students[highest_average_index].get_full_name()
    print(f"ყველაზე წარჩინებული სტუდენტი ჩემს კლასში არის ***{highest_average_student}*** "
          f"რადგანაც მას აქვს საშუალო ქულა -> {average_grades[highest_average_index]}")


# displays student with highest and lowest grade in passed subject
def display_highest_and_lowest_in_subject(students, subject):
    subject_grades = np.array([stu.subject_points[subject] for stu in students])
    highest_grade_index = np.argmax(subject_grades)
    lowest_grade_index = np.argmin(subject_grades)
    highest_grade_student = students[highest_grade_index].get_full_name()
    lowest_grade_student = students[lowest_grade_index].get_full_name()
    print(f"The student with the highest ~~{subject}~~ grade is {highest_grade_student} with a grade of"
          f" {subject_grades[highest_grade_index]}")
    print(f"The student with the lowest ~~{subject}~~ grade is {lowest_grade_student}"
          f" with a grade of {subject_grades[lowest_grade_index]}")


# displays students with above average grade in English
def display_above_average_in_english(students):
    english_grades = np.array([stu.subject_points['ENGLISH'] for stu in students])
    average_english_grade = np.mean(english_grades)
    above_average_students = [stu for stu in students if stu.subject_points['ENGLISH'] > average_english_grade]
    print("average english grade is", average_english_grade)
    for stu in above_average_students:
        print(f"{stu.get_full_name()} has an above average English grade of {stu.subject_points['ENGLISH']}")


# calculates standard deviation of grades in each subject
def calculate_standard_deviation(students):
    for subject in subjects.SUBJECTS.names():
        if subject == 'NOTHING':
            continue
        subject_grades = np.array([stu.subject_points[subject] for stu in students])
        std_dev = round(np.std(subject_grades))
        print(f"საშუალო ქულა საგანში ^^{subject}^^ არის  {std_dev}")


# main function
if __name__ == '__main__':
    my_students, my_table = generate_students_table(10)
    print("----------------------")
    display_highest_average(my_students)
    print("----------------------")
    display_highest_and_lowest_in_subject(my_students, 'ENGLISH')
    print("----------------------")
    display_highest_and_lowest_in_subject(my_students, 'MATH')
    print("----------------------")
    display_above_average_in_english(my_students)
    print("----------------------")
    calculate_standard_deviation(my_students)
    print("----------------------")
