# link to blocks: https://viewer.diagrams.net/?highlight=0000ff&edit=_blank&layers=1&nav=1&title=dz1_1_python.drawio#R7Vhdb9sgFP01lrZKnfyd5LFO0u1hk1pVWpdHGt%2FanrCxCEmc%2FfpdMMR2nWSptMyr1Jery4EL3AMHsC1vmlefOSnTbywGarl2XFnezHLdcThGK4FdDfhjtwYSnsU15DTAQ%2FYLNGhrdJ3FsOo0FIxRkZVdcMmKApaigxHO2bbb7JnR7qglSaAHPCwJ7aOPWSxSnZY7avAvkCWpGdkJJ3VNTkxjnckqJTHbtiBvbnlTzpiovbyaApXcGV7quNsjtfuJcSjEOQHsHm5GGx9Wt9dicX%2F3%2FXFCR9c6jQ2ha52wnqzYGQYgRkJ0kXGRsoQVhM4bNOJsXcQgh7Gx1LT5yliJoIPgTxBip1eXrAVDKBU51bX1mHKgo7lpaMXWfAknEjJ7hPAExIl27n4FcOcCy0HwHcZxoERkm%2B48iN5Dyb5dQzM6mulXsO70WUfqJjNpI9tCTsYj46ONlJ33VqbhXZK4TTMBDyVR9GxRjIc43gAXUJ1muc%2BKDnAnfh2itWx29rYRhmOwtCWK0L4Qj5MhNitUmfghwz8FurRo1cwq3bMq7EyhwHRbQbK4aNc1Yapk4v6iMNwzheENKQz3sDCUjWobKOsrO1ZSMbgbklxu%2BuJpVSruQoqJRk8cvUR6pjVa2%2FSFft1jLbi%2BBGdafK8ZY9SandOVsP2BfOztWrwaSuniuhJKgbKEkxw7K4FnSCzwl3V3TcWfdP%2BcVWDu1QudA44TDHwQmNfC%2B0lwxkngnXkS%2BEOeBF7vJFitcwSUbxMrQJEG0rXcSAPOS8BVwNFL0x7m0nSGvjUdp0fKu1hOiuAMsQRDisXviaXkLD6klquuVq7%2BZ6V49uBKGeRr6I0qJThTKeGQSgmOPjDxqRa1nplz%2FczExOW9M5WkKE299aeb3dXYZGiNhYdX5Ka1CrPWYz08cUz9q6%2FgLoX%2BBSnEYvODSNW1%2FrJ5898%3D

'''
Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.
'''

a = list(input('Введите трехзначное число: '))
sum = int(a[0]) + int(a[1]) + int(a[2])
prod = int(a[0]) * int(a[1]) * int(a[2])
print(f'Сумма цифр Вашего числа = {sum}, произведение = {prod}')