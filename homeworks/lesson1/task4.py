number = int(input('введите целое положительное число: '))
maxnumber = number % 10
number = number // 10
while number > 0:
    if number % 10 > maxnumber :
        maxnumber = number % 10
    number = number // 10
print(maxnumber)

#нашла решение в инете, но я никак не могу понять как это работает, думаю проблема в том,
#что у меня плохо с математикой (