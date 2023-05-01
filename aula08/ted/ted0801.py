#1. Faça um algoritmo para ler 20 números e armazenar em um vetor. Após a leitura total dos 20
#números, o algoritmo deve escrever esses 20 números lidos na ordem inversa.

vetor = []  

for i in range(20):
    num = int(input(f"Digite o {i+1}º número: "))
    vetor.append(num)  


print("Números lidos na ordem inversa:")
for i in range(19, -1, -1):
    print(vetor[i])



