# 2. Faça um programa que mostre as tabuadas dos números de 1 a 10.

x = 0
while x < 11:
    for i in range(0, 11):
        calc = x * i
        print(f'{x} X {i} = {calc}')

    x = 1 + x


