""""
Написать программу сложения и умножения двух шестнадцатеричных чисел.
При этом каждое число представляется как массив, элементы которого это цифры числа.
Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
"""

import collections


def dex_(val_dex):
    num = collections.deque()
    for v in list(val_dex):
        if v in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
            num.append(v)
        elif v == 'A':
            num.append(10)
        elif v == 'B':
            num.append(11)
        elif v == 'C':
            num.append(12)
        elif v == 'D':
            num.append(13)
        elif v == 'E':
            num.append(14)
        elif v == 'F':
            num.append(16)
        else:
            print("Вы ввели неверный символ в числе")
    dex_num = 0
    for i in range(len(num)):
        dex_num += int(num[i]) * (16 ** i)
    return (dex_num)


print(dex_('2A'))


def hex_(val_hex):
    num = collections.deque()
    while val_hex > 0:
        part_1 = val_hex % 16
        if part_1 in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
            num.append(part_1)
        elif part_1 == 10:
            num.append('A')
        elif part_1 == 11:
            num.append('B')
        elif part_1 == 12:
            num.append('C')
        elif part_1 == 13:
            num.append('D')
        elif part_1 == 14:
            num.append('E')
        elif part_1 == 15:
            num.append('F')
        val_hex //= 16
    # num.reverse()
    return list(num)

print(hex_(162))

num_1 = dex_(input('Введите первое число в шестнадцатиричном формате: ').upper())
num_2 = dex_(input('Введите второе число в шестнадцатиричном формате: ').upper())

print(f'Сумма чисел: {hex_(num_1 + num_2)}')
print(f'Произведение чисел: {hex_(num_1 * num_2)}')

# немного недоработал, занятие через 5 минут начнется.