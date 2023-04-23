#Dado uma lista de números, crie um algoritmo que retorne a soma dos números pares na lista.
#Exemplo de entrada: [1, 2, 3, 4, 5, 6]
#Saída esperada: 12


numeros = [1, 2, 3, 4, 5, 6]
soma = 0

for i in numeros:
    if i % 2 == 0:
        soma += i

print(soma)