""""
Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартала
(т.е. 4 отдельных числа) для каждого предприятия.. Программа должна определить среднюю прибыль
(за год для всех предприятий) и вывести наименования предприятий, чья прибыль выше среднего и
отдельно вывести наименования предприятий, чья прибыль ниже среднего.
"""

import collections

count_firms = int(input("Введите количество предприятий: "))
count_firms_2 = count_firms
firms = collections.defaultdict(list)
while count_firms > 0:
    named_firm = input('Введиете название предприятия: ')
    profits = [int(input(f"Введите прибыль за {i + 1} квартал ")) for i in range(4)]
    dict_ = {named_firm: profits}
    firms.update(dict_)
    count_firms = count_firms - 1
# print(firms)
dictProfit = {key: sum(l_values) for key, l_values in firms.items()}
# print((dictProfit))
all_profit = 0
for val in dictProfit.values():
    all_profit += float(val)
# print(all_profit)
mid_profit = all_profit / count_firms_2
for name, values in dictProfit.items():
    if values > mid_profit:
        print(f"Предприятие, чья прибыль выше среднего: {name}")
    else:
        print(f"Предприятие, чья прибыль равна или ниже среднего: {name}")


