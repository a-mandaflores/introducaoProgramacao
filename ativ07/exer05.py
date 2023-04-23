#Dado uma tupla de tuplas, onde cada tupla interna representa um intervalo de tempo (horário de início
#e horário de término), crie um algoritmo que retorne a quantidade de horas total dos intervalos.
#Exemplo de entrada: ((8, 12), (14, 18), (19, 22))
#Saída esperada: 11

#ini_horario = input('Insira o horario inicial: ')
#final_horario = input('Insira o horario final: ')

tupla_tuplas = ((8, 12), (14, 18), (19, 22))
result = []
index = len(tupla_tuplas)

i = 0

while i < index:
    sub = tupla_tuplas[i][1] - tupla_tuplas[i][0]
    result.append(sub)
    

    i += 1


print(sum(result))
#for i in tupla_tuplas:
#    print(slice.indices(tupla_tuplas))