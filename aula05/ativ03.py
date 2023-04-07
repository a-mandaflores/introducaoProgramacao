# 3. Armazene os nomes de alguns de seus amigos em uma lista chamada amigos. Exiba o nome de cada
# pessoa acessando cada elemento da lista um de cada vez.


amigos = []

qntAmangos = int(input('Quantos amigos você tem? '))

i = 1
while i <= qntAmangos:
    amigos.append(input('Qual o nome do seus amigos: '))
    i += 1

print(amigos)
