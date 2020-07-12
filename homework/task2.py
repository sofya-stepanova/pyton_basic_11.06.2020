class MyZeroDivisionError(Exception):
    def __init__(self, denominator):
        self.denominator = denominator


numenator = input('Введите числитель:')
denominator = input("Введите знаменатель: ")


try:
    denominator = int(denominator)
    numenator = int(numenator)
    if denominator == 0:
        raise MyZeroDivisionError("Ноль не может являться знаменателем, деление на ноль запрещено")
except ValueError:
    print("Вы ввели не число")
except MyZeroDivisionError as err:
    print(err)
else:
    result = numenator / denominator
    print(f"Результат деления {numenator} на {denominator}: {result}")