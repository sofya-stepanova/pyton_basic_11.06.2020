def int_func():
    user_input = input('введите слова через пробел:')
    sentence = user_input.split(' ')
    for i in sentence:
        print(i.capitalize(), end=' ')



int_func()


