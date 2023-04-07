# 4. Faça um programa que receba um número e que calcule e mostre a tabuada desse número..

num = int(input('Digite um numero para tabuada: '))
div = int(input('Dividir até quanto? '))
div1 = div + 1


for x in range(div1):
    calc = x * num
    print(f'{num} x {x} = {calc}')


