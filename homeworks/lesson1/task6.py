a = int(input('сколько километров составила пробежка в 1 день? '))
b = int(input('сколько километров вы хотели бы пробегать за одну пробежку? '))
day = 1

while a <= b:
    a = a + 0.1 * a
    day = day + 1
    print(a, day, 'день')
print('вы достигнете желаемого результата на {}  день'.format(day))

