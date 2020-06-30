class Road:
    def __init__(self, _lengh, _width):
        self._lengh = _lengh
        self._width = _width

    def calc(self):
        m = 12
        sm = 15
        result = self._lengh * self._width * m * sm
        return result






a = Road(200, 15)
print(a.calc())
