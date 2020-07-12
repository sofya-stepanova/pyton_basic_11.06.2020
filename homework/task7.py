class ComplexNumber:
    def __init__(self, real, image):
        self.real = real
        self.image = image

    def __str__(self):
        return f'{self.real} + {self.image} * i'

    def __add__(self, other):
        return f'{(self.real + other.real)} + {(self.image + other.image)}*i'

    def __mul__(self, other):
        return f'{(self.real * other.real - self.image * other.image)} + {(self.image * other.real + self.real * other.image)}*i'


complex = ComplexNumber(2, 3)
complex2 = ComplexNumber(4, 5)

assert complex + complex2 == '6 + 8*i'
assert complex * complex2 == '-7 + 22*i'