class Person:
    def __init__(self, name, surname, mark=1):
        self._name = name
        self._surname = surname
        self._mark = mark
    def get_info(self):
        return (f"{self._name}  {self._surname} його оцінка становить {self._mark}")
