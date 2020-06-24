list = [i for i in range(100, 1000) if not i & 1]

def reduce(x):
    result = 0
    for i in x:
        result += i
    return result


print(reduce(list))
