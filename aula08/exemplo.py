import random

n = int(input('Digite a dimensão: '))
m = int(input('Digite a dimensão: '))
matriz = []

for i in range(n):
    linha = []
    for j in range(m):
        linha.append(random.randint(0, 100))
    matriz.append(linha)

for l in matriz:
    print(l)

tamMatriz = int(len(matriz) / 2)
inteiro = tamMatriz - 1


print(matriz[inteiro][inteiro])
print(matriz[tamMatriz][tamMatriz])
