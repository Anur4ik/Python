from type_success import DesiredSuccess, RealSuccess


class StudentData:
    def __init__(self, student, subjects, real_grades, desired_grades):
        self.student = student
        self.real_success = RealSuccess(subjects, real_grades)
        self.desired_success = DesiredSuccess(subjects, desired_grades)

    def get_info(self):
        return {
            "ПІБ": self.student.get_pib(),
            "Група": self.student.get_group_number(),
            "Середній бал (реальний)": self.real_success.average_score(),
            "Середній бал (бажаний)": self.desired_success.average_score()
        }