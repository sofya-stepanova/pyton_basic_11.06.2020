import os
import json

with open(os.path.join(os.getcwd(), "task7.txt"), "r", encoding="UTF-8") as file:
    firms_dict = {}
    firms_profit = []
    costs = 0


    for line in file:
        line = line.split(" ")
        profit = int(line[2]) - int(line[3])
        if profit >= 0:
            firms_profit.append(profit)

        costs += int(line[3])
        firm = {line[0]: profit}
        firms_dict.update(firm)
        avg_profit = {"Средняя прибыль": sum(firms_profit) / sum(1 for line in open('task7.txt', 'r'))}


result_list = [firms_dict, avg_profit]

with open("file.json", "w", encoding='UTF-8') as write_file:
    json.dump(result_list, write_file)

print(firms_profit)
print(avg_profit)
print(firms_dict)
print(result_list)





