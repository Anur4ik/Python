from success import Success

class DesiredSuccess(Success):
    def __init__(self, subjects, desired_grades):
        super().__init__(subjects, desired_grades)

    def average_score(self):
        if len(self.grades) == 0:
            return 0
        return sum(self.grades) / len(self.grades)
class RealSuccess(Success):
    def __init__(self, subjects, desired_grades):
        super().__init__(subjects, desired_grades)

    def average_score(self):
        if len(self.grades) == 0:
            return 0
        return sum(self.grades) / len(self.grades)