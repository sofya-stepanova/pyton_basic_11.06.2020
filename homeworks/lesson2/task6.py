
base = []
position = int(input('сколько позиций товара вы будете вводить? '))
for i in range(position):
    name = input('введите наименование: ')
    price = input('введите цену: ')
    unit = input('введите единицу измерения товаров: ')
    quantity = input('введите количество товара:')
    new_dict = {'наименование': name,'цена': price,'единица измерения': unit,'количество товара': quantity}
    tup = (i+1, new_dict)
    base.append(tup)
print(base)

#дальше не смогла сообразить







