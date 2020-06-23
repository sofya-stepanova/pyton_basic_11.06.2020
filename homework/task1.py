try:
    def func(x, y):
        return x/y

except ZeroDivisionError:
    print('деление на ноль невозможно')