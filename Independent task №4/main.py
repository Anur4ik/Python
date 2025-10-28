from student import Student
from student_data import StudentData
from database import Database
db = Database()
student = Student("Котасов Олександр Сергійович", "ІСД-32", "2006-09-26", "м. Київ")
subjects = ["Математика", "Програмування", "Фізика"]
real_grades = [85, 90, 78]
desired_grades = [95, 98, 100]
data = StudentData(student, subjects, real_grades, desired_grades)
info= data.get_info()
print("Данні які були введені")
print( info)

db.insert_student(
    pib=data.student.get_pib(),
    group_number=data.student.get_group_number(),
    birth_date=data.student.get_birth_date(),
    avg_real=data.real_success.average_score(),
    avg_desired=data.desired_success.average_score(),
)

print("Всі студенти у БД:")
for row in db.get_all_students():
    print(row)
db.update_student(student_id=1, avg_real=88.5, avg_desired=99.0)
db.delete_student(2)
