"""
Матрица 5x4 заполняется вводом с клавиатуры, кроме последних элементов строк.
Программа должна вычислять сумму введенных элементов каждой строки и
записывать ее в ее последнюю ячейку.
В конце следует вывести полученную матрицу.
"""

ROW_NUM = 5
COL_NUM = 4
matrix = []
for i in range(ROW_NUM):
    row_ = []
    sum_ = 0

    for j in range(COL_NUM - 1):
        # num = int(input(f'{i}-я строка, {j}-й элемент : '))
        import random  # строка для тестирования
        num = random.randint(0, 10)  #  строка для тестирования
        sum_ += num
        row_.append(num)

    row_.append(sum_)
    matrix.append(row_)

for line in matrix:
    for item in line:
        print(f'{item:>8_}', end='')
    print()

# O(ROW_NUM*COL_NUM) -> O(N*M) - для прямоугольной матрицы
# O(N*N) = O(N**2) - для квадратной матрицы
