list1 = (input('введите несколько слов: '))
a = list1.split(' ')
for i, item in enumerate(a):
    print(i + 1, item[:10])

