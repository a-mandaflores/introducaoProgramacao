# 6. Seja criativo ao desenvolver este programa.

# a. Crie uma lista de convidados para um jantar em sua casa, com pelo menos 5 celebridades.

jantar = []

qntConvidados = int(input('Quantas pessoas vão para o jantar? '))

if qntConvidados >= 5:
    print(f'Você tem {qntConvidados} convidados')

    i = 1
    while i <= qntConvidados:
        nomeConvidados = jantar.append(input('Qual o nome dos convidados? '))
        i += 1

    # b. Envie um convite para cada uma dessas pessoas. Com a mesma mensagem e nome
    # personalizado.

    for i in jantar:
        print(f'Estou te convidando para meu jantar. {i}')

    # c. Sabendo que uma dessas pessoas não poderá ir ao seu jantar, você deverá enviar novos
    # convites. Imprima o nome das pessoas que não poderão comparecer.
    # d. Modifique sua lista, substitua os desistentes por novos convidados.

    qntDesistencia = int(input('Quantas pessoas desistiram? '))
    desistencia = []

    if qntDesistencia > 0:
        i = 1
        while i <= qntDesistencia:
            desistConvite = input('Digite o nome de quem desistiu do jantar: ')
            jantar.remove(desistConvite)
            desistencia.append(desistConvite)
            i += 1
        print(f'Essas pessoas desistiram do convite: ', desistencia)

        for i in desistencia:
            subst = input(f'Quem vc gostaria de substituir {i}: ')
            print(f'Estou te convidando para meu jantar. {subst}: ')

            jantar.append(subst)

        # novosConvites = input(f'Quem você quer que substitua {desistencia[quantDeDesistencia]}')
    else:
        print('Ninguem desistiu')

    # e. Exiba um novo convite para cada pessoa que continua presente em sua lista.

    print(jantar)
else:
    print('O jantar precisa ter pelo menos 5 celebridades')


