"""
Найти максимальный элемент среди минимальных элементов столбцов матрицы.
"""

import random

SIZE_ROW = 5
SIZE_COL = 4
MIN_ITEM = 0
MAX_ITEM = 100
matrix = [[random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE_COL)]
          for _ in range(SIZE_ROW)]

for line in matrix:
    print(*line, sep='\t')

max_ = None

for j, min_ in enumerate(matrix[0]):
    # for i in range(len(matrix)):
    #     if matrix[i][j] < min_:
    #         min_ = matrix[i][j]
    for i, line in enumerate(matrix):
        if line[j] < min_:
            min_ = line[j]

    if max_ is None or max_ < min_:
        max_ = min_

print(f'Max in min = {max_}')
