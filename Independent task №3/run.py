from employee import Employee
from manager import Manager

employee1 = Employee("Іван", 15000, 20, 10)
employee2 = Employee("Марія", 18000, 25, 5)

manager1 = Manager("Олена", 25000, 26, 15, 5)
manager2 = Manager("Андрій", 30000, 28, 20, 8)

team = [employee1, employee2, manager1, manager2]

for i in team:
    print(f"Працівник: {i.get_name()}")
    print(f"Зарплата: {i.calculate_monthly_salary():.2f} грн")
    print(f"Бонус: {i.bonus():.2f} грн")