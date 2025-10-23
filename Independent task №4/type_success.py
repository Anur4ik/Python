from success import Success

class DesiredSuccess(Success):
    def __init__(self, subjects, desired_grades):
        super().__init__(subjects, desired_grades)

    def average_score(self):
        if len(self.grades) == 0:
            return 0
        return round(sum(self.grades) / len(self.grades), 2)
class RealSuccess(Success):
    def __init__(self, subjects, desired_grades):
        super().__init__(subjects, desired_grades)

    def average_score(self):
        if len(self.grades) == 0:
            return 0
        return round(sum(self.grades) / len(self.grades), 2)