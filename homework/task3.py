class Cell:
    def __init__(self, count):
        self.__count = int(count)

    def __add__(self, other):
        return Cell(self.__count + other.__count)

    def __sub__(self, other):
        return Cell((self.__count - other.__count) if (self.__count - other.__count) > 0 else
                    print('невозможно провести операцию'))

    def __mul__(self, other):
        return Cell(self.__count * other.__count)

    def __truediv__(self, other):
        return Cell(self.__count//other.__count)

    def make_order(self, cells_in_lines):
        if type(cells_in_lines) is int:
            tmp = self.__count // cells_in_lines #количество рядов
            tmp2 = self.__count % cells_in_lines #количество оставшихся *
            result = '\n'.join(['*' * cells_in_lines] * tmp + ['*' * tmp2])
            return result
        else:
            print('число должно быть целым')


a = Cell(12)
b = Cell(10)
c = a + b
d = a - b
e = a * b
f = a / b
print(d.make_order(6))