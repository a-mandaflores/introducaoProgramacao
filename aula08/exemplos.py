nomes = ["Amanda", "Lari", "Miguel", "Joao"]

print(nomes[2])

print(type(nomes))
print(len(nomes))

frutas = ['pera', 'uva', 'maça', 'kiwi', 'Melancia']
print(frutas)

frutas[1] = 'abacate'
print(frutas)

frutas.insert(2, 'morango')

frutas.insert(5, 'chuchu')

print(frutas)

del frutas[5]
indice_fruta = frutas.index('morango')
print(frutas)

del frutas[indice_fruta]
print(frutas)

del frutas[frutas.index('Melancia')]

frutas.remove('kiwi')
print(frutas)

frutas.insert(10, 'Ameixa')
print(frutas)

pop_fruta = frutas.pop(frutas.index('Ameixa'))
print(pop_fruta)