"""
Определить, какое число в массиве встречается чаще всего.
"""
import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 15
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(f'Массив: {array}')

count_list = []
for i in array:
    count_num = 0
    for n in array:
        if i == n:
            count_num += 1
    count_list.append(array.index(i))


print(count_list)
