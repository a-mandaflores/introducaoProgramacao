max_estoque = int(input('Qual o maximo de estoque: '))
min_estoque = int(input('Qual o valor minimo de estoque: '))
estoque = int(input('Qual o valor de estoque: '))


calc_media = max_estoque + min_estoque
media = calc_media / 2
print(media)
if estoque > media:
    print('Não efetuar compra.')
else:
    print('Estoque abaixo da media.')