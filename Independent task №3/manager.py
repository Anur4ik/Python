from employee import Employee


class Manager(Employee):
    def __init__(self, name, salary, days_worked,bonus=0 ,number_of_subordinates=0):
        super().__init__(name,salary,days_worked,bonus)
        self.number_of_subordinates = number_of_subordinates

    def zvit(self):
        return (f"Менеджер {self.name} керує {self.number_of_subordinates} співробітниками.")