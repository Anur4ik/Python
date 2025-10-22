from student import Student
from student_data import StudentData

student = Student("Котасов Олександр Сергійович", "ІСД-32", "2006-09-26", "м. Київ")
subjects = ["Математика", "Програмування", "Фізика"]
real_grades = [85, 90, 78]
desired_grades = [95, 98, 100]
data = StudentData(student, subjects, real_grades, desired_grades)
print( data.get_info())