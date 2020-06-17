my_list = [7, 5, 3, 3, 2]
try:
    my_list.append(int(input('введите число: ')))
except ValueError:
    print('некорректный ввод')
my_list.sort(key=lambda number: number, reverse=True)
print(my_list)
