from random import randint

list = []

for i in range(20):
    list.append(randint(1, 100))

print(list)
list2 = []


def my_func(x):
    for i in range(0, len(x)):
        if x[i] > x[i-1]:
            list2.append(x[i])
    return list2

print(my_func(list))






