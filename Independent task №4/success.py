from abc import ABC, abstractmethod


class Success(ABC):
    def __init__(self, subjects, grades):
        self.subjects = subjects
        self.grades = grades

    @abstractmethod
    def average_score(self):
        pass