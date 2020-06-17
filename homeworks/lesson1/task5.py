revenue = input('выручка : ')
costs = input('издержки: ')

if revenue > costs :
    employees = input('сколько в штате сотрудников? ')
    profit = int(revenue) - int(costs)
    profitability = int(profit) / int(revenue)
    em_profit = int(profit) / int(employees)
    print('поздравляю, вы в плюсе! рентабельность составляет:', profitability ,
          'Прибыль на каждого сотрудника составила:' , em_profit)
else:
    print('вы работаете в убыток')