""""
link to blocks: https://viewer.diagrams.net/?highlight=0000ff&edit=_blank&layers=1&nav=1&title=dz_2.drawio#R7VpLk9soEP41riSHbAn09HH8yMwhqUrVVHaT0xa2GEuJJFwYx3Z%2B%2FYIEEgjb4%2FFEI%2B%2FEB1OigUbq7q%2Fpbjxwx%2Fn2lqJl8onEOBtAJ94O3MkAwiiIeCsIu4rgRbAiLGgaVyTQEO7TX1gSHUldpzFeGRMZIRlLlyZxTooCz5lBQ5SSjTntgWTmrku0wBbhfo4ym%2FpPGrNEfhYMG%2FodTheJ2hkEw2okR2qy%2FJJVgmKy0UjudOCOKSGsesq3Y5wJ2Sm5fAnu%2Fr5NwP1wegdvi%2FFsOP2C3lfMPjxlSf0JFBfsN7MO5LexnRIYjrn8ZBdnM7KZNoQRJesixoKjw3uEsoQsSIGyj4QsORFw4nfM2E7aAVozwkkJyzM5ircp%2ByqW%2F%2BXL3jdtZLKVnMvOTnUKRnfaItH9po81y8qeWld9mvielik8Ikc5b0XWdI6PzJNAYIgu8DF%2Bbm0sHGSY5Ji%2FJF9HcYZY%2BtN8OSTNfVHPa1TKH6RWn6Bh%2BZI%2FUbaWOw24cIYT0Y6cARd9FKpn3o7KdmpZRaN4oatNkjJ8v0SleDbcb5hKlltiyvD2DNHbopJcXFdCUfki2d00wAYKrYkG6sDpSLggvMLnbPi4J8LH6xM%2B7n74lO2oav2y9co2KgGl6LDClI41WLZu2Tom7jhlrM2fakxqkFb8gQlV502xzt9YlsjPq6V45ApDWYYzsqAo53pdYppy4WDaHvvcDDyG8Id0i9Vh3ynigW8gHuyDvP%2BikI%2BukD8b8t6JkPf7hLxnQX7Odcj%2BBQKKou9w2woy%2Fv6jGeVPC%2FFUTYH6lIMnqHM5J%2BgFHKHAkpSOpwYwV1AdA8sJoAp6DUOPJxodqxloSm5U%2FjrVDHt1nr7lPB8IFYvEr%2BAND1UORioJ3iKu4FaMIql1dAIvKDxpuVPXA6e506grdzrs1Zu%2BApgFJ8Is7BNlwA4vrt60EzVHfao5sJxpmXz6VhIYld6VvU3fqZzT01LTkZmaVmt5%2B6GdoEKnDGCt4LYcBhrHUK2cauygmeby5xvFN0C58NDFbLWsdauHxgnJZ%2BtVj2ExaBWWIt%2F248EePw7czuJi7yjEO8wzz0K3ge0G6j2hOzwR3c8NleTSz4SDT7OmYSsqAC0jqd5Lrmrs5IZStNOmLcWE1eF9QGTu4wOnZXYVx8YI62883y5Dyydp2TEclSTHzukuIvuFLZgHcA%2FMXzb7PR6vXQbKu0brc8%2FY09DhtmPu34XCllH57gugMDqAQvg%2FQKHnt1AY9l2DUpu1A60brRA%2FUeEPj27sWsZFXo9FsHfBHrg%2B8VRg2BIjFwgzZYWydFHw5zkXTHkxIcSWzlF2IwfyNI4r14hX6S80K1kJ65a45Xz90cCfCF7cG66aosCKUfIDj0lGRJWhIAXu8ugJzYsM5SV03bh7VAM7U41d5tYuhn0Zxf85CvLC%2FW5cV5D3ogo6frd8LYw%2F%2Fv%2BMk0umzn7TeFoE8tTAIRiaLiEMW3%2FgeSStaM3vJtCAdkFXXYBzBzHSrsGnsu4gKwP62akXIELNv%2Bh1A8XEuO72tQkTtSNv61vxQOPsyUt16LyVKUldDYnMSod%2F4haSD3xnIfE13K37LXvy94QLdcb0zHCBd5s%2FylW22fzb0J3%2BBw%3D%3D

Посчитать четные и нечетные цифры введенного натурального числа. Например, если введено число 34560,
то у него 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).
"""
num = input('Введите натуральное число: ')
count_1 = 0
count_2 = 0
for i in num:
    if int(i) % 2 == 0:
        count_1 += 1
    else:
        count_2 += 1
print(f'Количество четных цифр: {count_1}, количество нечетных цифр: {count_2}')


