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

db.insert_student(data.student.get_pib(),data.student.get_group_number(),data.student.get_birth_date(), data.real_success.average_score(), data.desired_success.average_score(),
)

print("Всі студенти у БД:")
for row in db.get_all_students():
    print(row)
db.update_student(1,'oleks')
db.delete_student(2)
