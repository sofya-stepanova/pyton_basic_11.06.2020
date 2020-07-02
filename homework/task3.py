import os

file_path = os.path.join(os.path.dirname(__file__), 'task3.txt')
my_dict = {}

with open (file_path, encoding='UTF-8') as file:
    for line in file:
        tmp = int(line.split(' ')[1])
        tmp1 = line.split(' ')
        name = tmp1[0].split(':')[0]
        my_dict[name] = tmp

print(my_dict)


def get_key(my_dict, value):
    for k, v in my_dict.items():
        if v == value:
            print(k)


for value  in my_dict.values():
    if value < 20000:
        get_key(my_dict, value)

a = []
for value in my_dict.values():
    a.append(value)

print(f'Cредняя заработная плата сотрудников составляет: {sum(a)/len(a)}')

