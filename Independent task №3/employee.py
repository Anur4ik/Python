class Employee:
    def __init__(self, name, salary, days_worked,bonus=0):
        self._name = name
        self._salary = salary
        self._days_worked = days_worked
        self._bonus = bonus
    def get_name(self):
        return self._name
    def get_salary(self):
        return self._salary
    def get_days_worked(self):
        return self._days_worked
    def get_bonus(self):
        return self._bonus
    def set_bonus(self, bonus):
        self._bonus = bonus
    def set_salary(self, salary):
        self._salary = salary
    def set_days_worked(self, days_worked):
        self._days_worked = days_worked
    def set_name(self, name):
        self._name = name

    def calculate_monthly_salary(self):
       return (self._salary/ 30) * self._days_worked

    def bonus(self):
        return (self.calculate_monthly_salary() / 100) * self._bonus
