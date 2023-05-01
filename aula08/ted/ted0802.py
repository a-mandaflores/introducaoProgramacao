vetor = []  

for i in range(10):
    num = int(input(f"Digite o {i+1}º número: "))
    vetor.append(num) 

repetidos = [] 
for i in range(len(vetor)):
    if vetor[i] in vetor[i+1:] and vetor[i] not in repetidos:
        repetidos.append(vetor[i])

if len(repetidos) == 0:
    print("Não há números repetidos no vetor.")
else:
    print("Números repetidos no vetor:")
    for num in repetidos:
        print(f"O número {num} se repete nas posições:", end=" ")
        for i in range(len(vetor)):
            if vetor[i] == num:
                print(i, end=" ")
        print()