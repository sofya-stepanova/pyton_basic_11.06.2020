def insert_sum(*args):
    result = 0
    exit_flag = False
    for i in args:
        try:
            result += float(i)
        except ValueError:
            if i == 'q':
                exit_flag = not exit_flag
                break
    return result, exit_flag
user_sum = 0
user_exit = False
while not user_exit:
    user_input = input('вводите числа через пробел: ').split(' ')
    res_sum, user_exit = insert_sum(*user_input)
    user_sum += res_sum
    print(user_sum)
