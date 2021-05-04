"""
В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.
"""


count2, count3, count4, count5, count6, count7, count8, count9 = 0, 0, 0, 0, 0, 0, 0, 0
for n in range(2, 100):
    if n % 2 == 0:
        count2 += 1
for n in range(2, 100):
    if n % 3 == 0:
        count3 += 1
for n in range(2, 100):
    if n % 4 == 0:
        count4 += 1
for n in range(2, 100):
    if n % 5 == 0:
        count5 += 1
for n in range(2, 100):
    if n % 6 == 0:
        count6 += 1
for n in range(2, 100):
    if n % 7 == 0:
        count7 += 1
for n in range(2, 100):
    if n % 8 == 0:
        count8 += 1
for n in range(2, 100):
    if n % 9 == 0:
        count9 += 1
print(f' кратны 2 - {count2} \n кратны 3 - {count3} \n кратны 4 - {count4} \n кратны 5 - {count5} \n '
      f'кратны 6 - {count6} \n кратны 7 - {count7} \n кратны 8 - {count8} \n кратны 9 - {count9}')
