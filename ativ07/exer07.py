#Dado duas listas, crie um algoritmo que retorne a interseção dos elementos das duas listas (ou seja, os
#elementos que aparecem nas duas listas).
#Exemplo de entrada: [1, 2, 3, 4], [3, 4, 5, 6]
#Saída esperada: [3, 4]

entradaA = [1, 2, 3, 4]
entradaB = [3, 4, 5, 6]
novaLista = []

for i in entradaA:
    if i in entradaB:
        novaLista.append(i)

     
print(novaLista)