class Worker:
    _income = {'wage': 110000, 'bonus': 30000}

    def __init__(self, name, surname, position):
        self.name = name
        self.surname = surname
        self.position = position


class Position(Worker):

    def get_full_name(self):
        print(f'{self.name} {self.surname}')

    def get_full_income(self):
        print(self._income['wage'] + self._income['bonus'])

a = Position( 'sofya', 'stepanova', 'skylower')
a.get_full_name()
a.get_full_income()

