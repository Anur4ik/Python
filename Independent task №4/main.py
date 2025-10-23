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
print( info)

db.insert_student(
    pib=info["ПІБ"],
    group_number=info["Група"],
    birth_date=info,
    avg_real=info["Середній бал (реальний)"],
    avg_desired=info["Середній бал (бажаний)"]
)

# Перевіряємо
print("\nВсі студенти у БД:")
for row in db.get_all_students():
    print(row)