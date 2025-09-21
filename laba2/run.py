
from FullTimeStudent import FullTimeStudent
from PartTimeStudent import PartTimeStudent
student1 = FullTimeStudent("KOLA", 24, 910, 10, 95, 85)
student2 = FullTimeStudent("Klavdia Petrivna", 19, 930, 10, 99, 20)
student3 = PartTimeStudent("CHEEV", 22, 390, 4, 78)
student4 = PartTimeStudent("YAKTAK", 21, 480, 5, 82)

university_students = [student1, student2, student3, student4]

for student in university_students:
    student.display_info()
    if isinstance(student, FullTimeStudent):
        print(f"Загальний бал: {student.total_score()}")
    elif isinstance(student, PartTimeStudent):
        print(f"Загальний бал (заочно): {student.total_score()}")
    print("---------")


