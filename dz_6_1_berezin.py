""""
Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках
первых трех уроков. Проанализировать результат и определить программы с наиболее эффективным
использованием памяти.
    Примечание: Для анализа возьмите любые 1-3 ваших программы или несколько вариантов
кода для одной и той же задачи. Результаты анализа вставьте в виде комментариев к коду.
Также укажите в комментариях версию Python и разрядность вашей ОС.

Задача для анализа: Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести
на экран. Например, если введено число 3486, то надо вывести число 6843
"""
# print(sys.version) -> python 3.8.5, 64 bit.

import sys
import random

# # вариант 1
num_1 = int(input("Введите число: "))
k = 0
sum_ = 0
while num_1 > 0:
    k = k * 10 + num_1 % 10
    num_1 = num_1 // 10
    sum_ += sys.getsizeof(num_1 + k)
print(f'Количество занимаемой памяти в первом случае: {sum_} байт')


# Результат первой задачи, вариант 1:
# Введите число: 1234
# Количество занимаемой памяти в третьем случае: 112 байт

# Программа для анализа
def show(obj, step=0):
    print(f'{type(obj)=}, {sys.getsizeof(obj)=}, {obj=}')
    size_ = sys.getsizeof(obj)
    if hasattr(obj, '__iter__'):
        if hasattr(obj, 'items'):
            for key, value in obj.items():
                show(key, step + 1)
                size_ += sys.getsizeof(key)
                show(value, step + 1)
                size_ += sys.getsizeof(value)
        else:
            for item in obj:
                show(item, step + 1)
                size_ += sys.getsizeof(item)
    return size_


# # # вариант 2
# '''
# Как только не пробовал этот вариант разобрать, не получается проверить через функцую show
# Если подскажете в чем проблема, буду признателен!
# Поэтому рассмотрю еще один пример в самом конце.
# '''
#
#
# # num_2 = input("Введите число: ")
# # itter_num_2 = [x for x in num_2[::-1]]
# # print(show(itter_num_2))

# вариант 3
def reverse_3(number, res=0, sum_=0):
    if number == 0:
        return (res, sum_)
    res = res * 10 + number % 10
    number = number // 10
    sum_ += sys.getsizeof(res + number)
    return reverse_3(number, res, sum_)


number = int(input("Введите число: "))
answer_of_fun = reverse_3(number)
print(f'Количество занимаемой памяти в третьем случае: {answer_of_fun[1]} байт')

# Результат первой задачи, вариант 3:
# Введите число: 1234
# Количество занимаемой памяти в первом случае: 112 байт


'''
Пример 2 (3 практическое занятие, 2 задача): 
Во втором массиве сохранить индексы четных элементов первого массива. 
Например, если дан массив со значениями 8, 3, 15, 6, 4, 2, то 
во второй массив надо заполнить значениями 1, 4, 5, 6 (или 0, 3, 4, 5 - если индексация начинается с нуля),
т.к. именно в этих позициях первого массива стоят четные числа.
'''

BASE = range(9)

array = [random.randint(1, 100) for n in BASE]
print(f'Массив: {array}')

array_index = [array.index(i) for i in array if i % 2 == 0]
print(f'Массив индексов четных элементов: {array_index}')

sum_ = show(array) + show(array_index) + show(BASE)
print(f'В программе задействовано байт памяти: {sum_}')

# Результат примера 2:
# Массив: [45, 25, 100, 29, 39, 11, 31, 36, 18]
# Массив индексов четных элементов: [2, 7, 8]
# type(obj)=<class 'list'>, sys.getsizeof(obj)=184, obj=[45, 25, 100, 29, 39, 11, 31, 36, 18]
# type(obj)=<class 'int'>, sys.getsizeof(obj)=28, obj=45
# type(obj)=<class 'int'>, sys.getsizeof(obj)=28, obj=25
# type(obj)=<class 'int'>, sys.getsizeof(obj)=28, obj=100
# type(obj)=<class 'int'>, sys.getsizeof(obj)=28, obj=29
# type(obj)=<class 'int'>, sys.getsizeof(obj)=28, obj=39
# type(obj)=<class 'int'>, sys.getsizeof(obj)=28, obj=11
# type(obj)=<class 'int'>, sys.getsizeof(obj)=28, obj=31
# type(obj)=<class 'int'>, sys.getsizeof(obj)=28, obj=36
# type(obj)=<class 'int'>, sys.getsizeof(obj)=28, obj=18
# type(obj)=<class 'list'>, sys.getsizeof(obj)=88, obj=[2, 7, 8]
# type(obj)=<class 'int'>, sys.getsizeof(obj)=28, obj=2
# type(obj)=<class 'int'>, sys.getsizeof(obj)=28, obj=7
# type(obj)=<class 'int'>, sys.getsizeof(obj)=28, obj=8
# type(obj)=<class 'range'>, sys.getsizeof(obj)=48, obj=range(0, 9)
# type(obj)=<class 'int'>, sys.getsizeof(obj)=24, obj=0
# type(obj)=<class 'int'>, sys.getsizeof(obj)=28, obj=1
# type(obj)=<class 'int'>, sys.getsizeof(obj)=28, obj=2
# type(obj)=<class 'int'>, sys.getsizeof(obj)=28, obj=3
# type(obj)=<class 'int'>, sys.getsizeof(obj)=28, obj=4
# type(obj)=<class 'int'>, sys.getsizeof(obj)=28, obj=5
# type(obj)=<class 'int'>, sys.getsizeof(obj)=28, obj=6
# type(obj)=<class 'int'>, sys.getsizeof(obj)=28, obj=7
# type(obj)=<class 'int'>, sys.getsizeof(obj)=28, obj=8
# В программе задействовано байт памяти: 904

'''
Проанализировав программы, могу сказать, что в первых двух вариантов первой задачи результат один и тот же, 
склоняюсь к тому, что если бы работала третья реализация, то объем памяти был бы больше, так как один строчный
символ занимает память в 50 байт, а значение занимает 28 байт.
'''
