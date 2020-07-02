import os
import random

file_path = os.path.join(os.path.dirname(__file__), 'task5.txt')
numbers = [random.randint(1, 100) for i in range (random.randint(1, 100))]

with open (file_path, 'w', encoding = 'UTF-8') as file:
    file.write(' '.join(map(str, numbers)))

with open (file_path, 'r', encoding = 'UTF-8') as file:
    num = map(int, file.read().split(' '))


print(sum(num))