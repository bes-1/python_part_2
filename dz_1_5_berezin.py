# link to blocks: https://viewer.diagrams.net/?highlight=0000ff&edit=_blank&layers=1&nav=1&title=dz1_1_python.drawio#R7Vpbc9soFP41nuk%2BpCN096NvSafb7nQmD7vtyw6SiKxWElqMa7u%2FfrnpgiTHSRNbieOHEHGAA3znwjmYkTXLtjcEFsvPOELpyDSi7ciaj0zTd31WcsJOEmzflISYJJEkgZpwm%2FxCimgo6jqJ0ErrSDFOaVLoxBDnOQqpRoOE4I3e7Q6n%2BqwFjFGHcBvCtEv9O4noUm3L9Gr6B5TEy3Jm4I5lSwbLzmonqyWM8KZBshYja0YwpvIr285QyrErcbm%2BmU%2F%2FCn%2B4xs23j9%2B2fy6iYvzvlWR2%2FZgh1RYIyunzsi7hWdFdCRiKGH6qigld4hjnMF3U1CnB6zxCnK3BanWfTxgXjAgY8TuidKeUAa4pZqQlzVLVirYJ%2FYcPf%2B%2Bo2tdGy3yrOIvKrqzklOwag3j1a7OtHiZq5Ti5P76plj4cALMEBq9JiO5DUOk0JDG6j59VaQyzNIQzxBbJxhGUQpr81BcHlc7HVb9aruxDifYxYpZ8f8J0rWYaMXDGc15OjRGD3vfKb1ZORbnoqEYteC6rzTKh6LaAAp4Ncx66kNWUiFC0%2FQ3ou1ApLqah7LF0SKq6qa0blCa7bFi2axwLXOtiQ0%2BzIeuBNmQPaUNWvw2JcipLR5S2KH1hVSXdNMoqKw3VwWxanuwPGvZn8F2MzFnA%2FsKOirHTqOCfTAgwTVGKYwIzJqsCkYRtGJF225e64ZDp3iVbVB7lxzRl4OumDKweW3ZPacvuoKbcMOTarF%2BXKdsPNGVnSFMeDyll8Iak7A8pZbvrsE03pdxHEqSJ3%2F1vzYP46R3O6dUdzJKUATnh%2Ftl0YVYIQC3LliIOCEzyFU8QcI47HcSgmWpdCQ9bsWdfsfovlsGa8951BDD8EQuFuwpxiolcDImDd6bjVDO0vv%2FomYgfUE7nYOEnT1CtXCwF6tVQ7j2VzK7lQvXFM7KAUae%2BJWT5ka1hekHsHsTCexUueCR27cRkibNgvRouKQGeo0Uy1aVBM5LxeiKZKlV5dvcHBj3lHpOWHPu0emqsoYZ%2BwQlbTp2Hunrw6tgtScrTUY2qhTkhBO4a3QreYbV%2Fnioobs1T64bkWGtKtcffVx6nN9mZgEb%2B0kx25g1Klezsy2sWMq85w3zG0yVlDX414fXnrHaZX7ZkwOCgOnIwTeKcfYcMFoE0By0JYTpRDVkSRdJzoFXyCwaCFTdqpdaMrzMdOXPOizmL1QmSSrvlit2uFKweIRzPEQ97P3QG6Yb%2FwHQD7NGM0%2BQbwH6NaaXrNSV9Zbw3gHdA3KLWcL8vSwfMIXXAv%2BSc%2B3POnpj%2FknM%2BLee8wLUfrkMTnWzDh9R66BW2UvOeq6EDWvYaM3YLtIL1vt8eTpyxG%2F3hepVdiV%2BQzjJotxxdGn1Bu33SoN0fNGh%2FQbcnoHy1czDy8gaNvsGRryyCs7yy6LymGPzOonpudbG8p6Yyw15cVnxPeXEJzCO7gfN8iWH7L80NgP4r6PO%2BuzRbPyNZXlcMp727dN9sSGqPjYOyOG1Iuuc2f6J8k%2BbOmFy6b5le5PtNpwfX53I1rFq%2Fz5ZHTP3I3Vr8Dw%3D%3D

'''
Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).
'''

a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
c = int(input('Введите третье число: '))
if b < a < c or c < a < b:
    print(f'Среднее число: {a}')
elif a < b < c or c < b < a:
    print(f'Среднее число: {b}')
else:
    print(f'Среднее число: {c}')

