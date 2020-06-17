my_list = []
stop = '.'
print('Из введенных вами значений будет сформирован список. Чтобы завершить формирование списка введите "."')
while stop:
    if stop in my_list:
        break
    my_list.append(input('введите что угодно: '))

for i in range(1, len(my_list), 2):
    my_list[i - 1], my_list[i] = my_list[i], my_list[i - 1]
print(my_list)


