"""
В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
"""
import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(f'Массив: {array}')

max_num = array[0]
min_num = array[0]
for i in array:
    if i > max_num:
        max_num = i
        inx_max = array.index(i)
    elif i < min_num:
        min_num = i
        inx_min = array.index(i)
array[inx_max], array[inx_min] = array[inx_min], array[inx_max]
print(f'Массив после изменения: {array}')
