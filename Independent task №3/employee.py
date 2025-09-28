class Employee:
    def __init__(self, name, salary, days_worked,bonus=0):
        self.name = name
        self.salary = salary
        self.days_worked = days_worked
        self.bonus = bonus

    def calculate_monthly_salary(self):
       return (self.salary/ 30) * self.days_worked

    def bonus(self):
        return (self.calculate_monthly_salary() / 100) * self.bonus
