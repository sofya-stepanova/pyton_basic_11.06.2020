from itertools import cycle, count

for i in count(3):
    if i > 10:
        break
    else:
        print(i)

list = [1, 2, 3, 4]
count = 0
for item in cycle(list):
    if count > 7:
        break
    print(item)
    count += 1
