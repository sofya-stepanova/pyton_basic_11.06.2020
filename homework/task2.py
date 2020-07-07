from abc import ABC, abstractmethod


class Clothes(ABC):
    @property
    @abstractmethod
    def consumption(self):
        pass


class Coat(Clothes):
    def __init__(self, size):
            self.__size = size

    @property
    def consumption(self):
        consumption = self.__size/6.5 + 0.5
        return consumption


class Costume(Clothes):
    def __init__(self, growth):
        self.__growth = growth

    @property
    def consumption(self):
        consumption = self.__growth * 2 + 0.3
        return consumption


a = Coat(46)
b = Costume(180)

print(a.consumption())
#выдает ошибку TypeError: 'float' object is not callable , она появилась после добавления @property
#я пробовала использовать конструкции как у вас -> float , size: float. Все равно не работает
#пожалуйста обьясните почему так
