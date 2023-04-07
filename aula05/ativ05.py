# 5. Utilizando a lista do exercício anterior, exiba uma saudação ("Olá como vai você"), personalizado
# com o nome de cada amigo. A saudação deve ser a mesma, alterando apenas o nome do amigo.

amigos = []

qntAmigos = int(input('Quantos amigos vai a festa?'))

i = 1
while i <= qntAmigos:
    amigos.append(input('Nome do seu amigo'))
    i += 1

for i in amigos:
    print(f'Bem vindo a festa {i}')
