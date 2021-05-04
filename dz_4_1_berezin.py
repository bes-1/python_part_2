""""
Проанализировать скорость и сложность одного любого алгоритма, разработанных в рамках домашнего задания
первых трех уроков.
    Примечание: попробуйте написать несколько реализаций алгоритма и сравнить их.
Задача 3 к уроку 2:
Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
Например, если введено число 3486, то надо вывести число 6843
"""

import timeit
import cProfile

# вариант 1
def reverse_1(num_1):
    k = 0
    while num_1 > 0:
        k = k * 10 + num_1 % 10
        num_1 = num_1 // 10
    return (k)


print(timeit.timeit('reverse_1(123)', number=100, globals=globals()))  # 8.219999999999061e-05
print(timeit.timeit('reverse_1(123456)', number=100, globals=globals()))  # 0.00014449999999999186
print(timeit.timeit('reverse_1(123456789)', number=100, globals=globals()))  # 0.0002178999999999931
cProfile.run('reverse_1(123)')
cProfile.run('reverse_1(123456)')
cProfile.run('reverse_1(123456789)')

"""
Во всех трех случаях:
4 function calls in 0.000 seconds
Ordered by: standard name
ncalls  tottime  percall  cumtime  percall filename:lineno(function)
    1    0.000    0.000    0.000    0.000 <string>:1(<module>)
    1    0.000    0.000    0.000    0.000 dz_4_1_berezin.py:11(reverse_1)
    1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
    1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
"""


# вариант 2
def reverse_2(num_1):
    result = num_1[::-1]
    return (result)


print(timeit.timeit('reverse_2("123")', number=100, globals=globals()))  # 3.9400000000001933e-05
print(timeit.timeit('reverse_2("123456")', number=100, globals=globals()))  # 3.1299999999997996e-05
print(timeit.timeit('reverse_2("123456789")', number=100, globals=globals()))  # 3.1799999999998496e-05
cProfile.run('reverse_2("123")')
cProfile.run('reverse_2("123456")')
cProfile.run('reverse_2("123456789")')

"""
Во всех трех случаях:
4 function calls in 0.000 seconds
Ordered by: standard name
ncalls  tottime  percall  cumtime  percall filename:lineno(function)
    1    0.000    0.000    0.000    0.000 <string>:1(<module>)
    1    0.000    0.000    0.000    0.000 dz_4_1_berezin.py:11(reverse_1)
    1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
    1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
"""


# вариант 3
def reverse_3(number, res=0):
    if number == 0:
        return res
    res = res * 10 + number % 10
    number = number // 10
    return reverse_3(number, res)


print(timeit.timeit('reverse_3(123)', number=100, globals=globals()))  # 0.0002062000000000036
print(timeit.timeit('reverse_3(123456)', number=100, globals=globals()))  # 0.0002723000000000031
print(timeit.timeit('reverse_3(123456789)', number=100, globals=globals()))  # 0.00036309999999999815
cProfile.run('reverse_3(123)')
cProfile.run('reverse_3(123456)')
cProfile.run('reverse_3(123456789)')

"""
Во всех трех случаях, только N менялась на 4, 7 и 10:
4 function calls in 0.000 seconds
Ordered by: standard name
ncalls  tottime  percall  cumtime  percall filename:lineno(function)
    1    0.000    0.000    0.000    0.000 <string>:1(<module>)
    N/1    0.000    0.000    0.000    0.000 dz_4_1_berezin.py:11(reverse_1)
    1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
    1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
"""

"""
Вывод:
    При реализации задачи тремя разными способами, видно, что второй вариант имеет быстродействие большее по
    сравнению с двумя другими. Самое медленная реализация у способа №3 (с рекурсией). 
"""