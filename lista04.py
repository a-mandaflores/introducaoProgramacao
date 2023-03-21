valor1 = int(input('Digite um valor: '))
valor2 = int(input('Digite outro valor: '))

if valor1 < valor2:
    print(valor2, valor1)
elif valor1 == valor2:
    print('Valores iguais')
else:
    print(valor1, valor2)