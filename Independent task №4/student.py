class Student:
    def __init__(self, pib, group_number, birth_date="", address=""):
        self.__pib = pib
        self.__group_number = group_number
        self.__birth_date = birth_date
        self.__address = address

    def get_pib(self):
        return self.__pib

    def get_group_number(self):
        return self.__group_number

    def get_birth_date(self):
        return self.__birth_date

    def get_address(self):
        return self.__address

    def set_pib(self, pib):
        self.__pib = pib

    def set_group_number(self, group_number):
        self.__group_number = group_number

    def set_birth_date(self, birth_date):
        self.__birth_date = birth_date

    def set_address(self, address):
        self.__address = address