import math

def func(x):
    for i in range(x):
        yield math.factorial(i+1)

for i in func(4):
    print(i)






