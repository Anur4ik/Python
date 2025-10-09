from employee import Employee
from manager import Manager

employee1 = Employee("Олексій", 15000, 20, 10)
employee2 = Employee("Денис", 15000, 25, 5)
employee3 = Employee("Владислав", 15300, 25, 5)
manager1 = Manager("Олександр", 40000, 15, 15, 10)
manager2 = Manager("Андрій", 25000, 20, 20, 8)

team = [employee1, employee2, manager1, manager2]

for i in team:
    if isinstance(i, Manager):
        print(f"Менджер : {i.get_name()}")
        print(i.zvit())
    else:
        print(f"Працівник: {i.get_name()}")
    print(f"Зарплата: {i.calculate_monthly_salary():.2f} грн")
    print(f"Бонус: {i.bonus():.2f} грн")
    print("-------------------------------")