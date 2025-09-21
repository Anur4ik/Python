from abc import ABC, abstractmethod
class Person(ABC):
    def __init__(self, name, age, prac_score, prac_count, exam_scr):
        self.name = name
        self.age = age
        self.prac_score = prac_score
        self.prac_count = prac_count
        self.exam_scr = exam_scr

    def avg_practice_score(self):
        if self.prac_count != 0:
            avg_prac = self.prac_score / self.prac_count
        else:
            avg_prac = 0
        return avg_prac
