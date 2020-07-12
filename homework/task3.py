class DataError(Exception):
    def __init__(self, data):
        self.data = data


list = []

while True:
    input_data = input('введите целое число: ')
    if input_data == 'stop':
        break
    try:
        if not input_data.isdigit():
            raise DataError ('Это не целое число!')
        input_data = int(input_data)
        list.append(input_data)
    except DataError as err:
        print(err)

print(list)













