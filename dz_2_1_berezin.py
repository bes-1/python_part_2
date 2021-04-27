""""
link to blocks: https://viewer.diagrams.net/?highlight=0000ff&edit=_blank&layers=1&nav=1&title=dz_2.drawio#R7Vtbc6M2FP4tefC43Rl3QOLmx%2FiSdCbd2XTSTpO%2ByUbBbDFiZBzb%2BfUVIIxAGJwYg5PdB2vg6BxA56bvHHAPjpfbW4qCxVdiY68HFHvbg5MeAJZhsTEi7BKCauhqQnGoa3NaRnhwXzEnKpy6dm28yjGGhHihG%2BSJc%2BL7eB7maIhSssmzPRMvf9cAOVgiPMyRJ1P%2Fce1wwdcFzIz%2BO3adRXpn1RgmM0uUMvOVrBbIJhuBBKc9OKaEhMnRcjvGXqS8VC%2BJ3M2B2f2DUeyHxwg4zvPXv%2B6Cv%2B0n8K%2Blz27xn%2FR1wB92Fe7SBWObrZ%2BfEhouiEN85E0z6oiStW%2Fj6KoKO8t4%2FiAkYESVEb%2FjMNxxY6J1SBhpES49Pou3bvgYif%2Bm87MnYWay5VeOT3b8RF4tV8CKrOkcVywx9RpEHRxW8IGEL1q%2FcAOuy1tMljikO8ZAsYdC9yXvH4i7mbPnyyzBDrgx3mAYft0X5K35nXpMD8NJNI6UHtOWZabHbBzF41SyZmarSL2bhRvihwDF%2BtqwgM3b5aCOXzAN8bZSK3wWKtzbebwPVFXnlE0WPmoaEwshdAzlXKpUJLVcqJMzvdOdIBSdPolzmVh8dnpwgCODQ7uo4ADlwRGPo2TU41GLRysOl5QOFGEK8BgCYkgl%2FKoQWLIHsWweRIdM6cjzsEccipbMFAGmLlskpsW5%2B2yiLg6f3S1Ot8KG4hKYJnOpfGQqZZFp6C1GJtR%2BRmZNxNVGpmpeVGhqDYTmNB5vUmbGoAjbniEIsg1P6ZOgH0kCw2N6Gs0oO3Kio5hvImySWn2YR%2BOYzwLllx5gFhwP2O8L%2BzGF%2FPoJE8Gw8zxgdpkGVCEJZCmhaRSqHxnORtPRHIteU4p2AkNAXD9cCVe%2BjwiZl2hmAcZpQ120cr0ANJRKgXT%2BkAA7SB4686r96k%2BAgrDS07A3I5vz7DVtOlnDzlNvO1UxC6kh8XMul1n1rX5YvJEFq71qX2zvcxtswav08j1Pl%2FYXS9iuIj6l%2F60vOSRdkOVsveqmXNOPrdZU9VybgVGuzWsBGkwEaGDICuy65gVW1yWvVa5D7UAxwxYa5tWCPNfx2fGcqSVGKpE63DnyrvnE0rXtJEXilfuKZvGlouzFQ5pdVx%2F19El0LZYVVxmIWYWU%2FIfHxCMRNPKJj5sxgwYKuEYHshlgiRXA2RoPBxKD6L7gcxoD6MXEUmIMrU1jgOqt%2F9y15hv2%2F%2FZrzbSGrO%2BRqk0jjNP6B3Lyv9DC4YJtChtHjaclTfM0NKWktb3IV2wN5MVYlf8%2BwcH7xL4cFEPLCJ74s1UQ277usW%2B6RY8yPDc0KckDpQw9QnCulFDd7P%2FoFV7zCfjIEm94pgpPLYJns40%2BwN7X5TYlSzIjoVk55Z1DeM1jds%2FDQ1jubGbZKV%2BsiGz7nuZEuOMwFalugO4fLKYXvf2D9SPVImo3FVPKIarVZjcSHOhh%2Fwiwvdg%2FsbqG7RCWG%2BNzl7KGXm%2BGVktZaP1E2nUAuh5pX9irum6%2Fi%2FhwNh0E6tr9%2FvBt601f7h4X47un%2B8dBV3jMTPsZNXisKcQET2hyJ4WKkodFWgliyt6%2BTrM3wvE1ZFdts9DRJO2blgxS2m2Ta129ymrnfWnzufLod1npF5wNVzpmsSVq6S1UOvBAO%2BWYSmeSD1HGnwSnGR%2FfVEZyUqfEIrk6KPrUSrm6upKc94PVLbpVsKZhyBCt3Zc%2BcPgDQmXdKtaPWsdQWav8dPdTl4%2BaqtUb41zlYyk8kxX9KT8wLOyStVtuFZStLWP0Ezfikwz6vsZdH%2FUzVNqfyW3z9ncfKapKjHb8JweGcSQgfcfuw06zf6kkuCT7rw%2Bc%2Fg8%3D

Написать программу, которая будет складывать, вычитать, умножать или делить два числа. Числа и знак операции
вводятся пользователем. После выполнения вычисления программа не должна завершаться, а должна запрашивать
новые данные для вычислений. Завершение программы должно выполняться при вводе символа '0' в качестве знака
операции. Если пользователь вводит неверный знак (не '0', '+', '-', '*', '/'), то программа должна сообщать
ему об ошибке и снова запрашивать знак операции. Также сообщать пользователю о невозможности деления на ноль,
если он ввел 0 в качестве делителя.
"""
while True:
    op = input('Введите операцию над числами (+, -, * или /) или "O", чтобы выйти из программы: ')
    if op == 'O': break
    if op in ('+', '-', '*', '/'):
        a = float(input("Введите число a: "))
        b = float(input("Введите число b: "))
        if op == '+':
            print(f'a+b = {a + b:.2f}')
        elif op == '-':
            print(f'a-b = {a - b:.2f}')
        elif op == '*':
            print(f'a*b = {a * b:.2f}')
        elif op == '/':
            if b != 0:
                print(f'a/b = {a / b:.2f}')
            else:
                print("Вы ввели делитель = 0, нельзя!")
    else:
        print("Вы ввели неверную операцию!")
