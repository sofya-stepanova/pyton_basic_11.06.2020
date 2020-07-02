import os


file_path = os.path.join(os.path.dirname(__file__), 'task6.txt')

my_dict = {}

with open (file_path, 'r') as file:
    for line in file:
        tmp = line.split(' ')
        name = tmp[0].split(':')[0]
        my_dict[name] = tmp[1:]

result = {}
for key, value in my_dict.items():
    result[key] = sum([int(itm.split('(')[0]) for itm in value if itm.split('(')[0].isdigit()])

print(result)