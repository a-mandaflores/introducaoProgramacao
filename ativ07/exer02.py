#Use um dicionário para armazenar os números favoritos de algumas pessoas. Escolha cinco colegas, e
#pergunte quais seus número favoritos. Use seus nomes para serem as chaves de cada número favorito.
#Ao final, exiba o nome de cada pessoas e seu número favorito.

amigos = {}

nome = input('Qual seu nome: ')
numero_fav = input('Qual seu numero favorito? ')

amigos[nome] = numero_fav

amigostrue = True

while amigostrue == True:
    sim_nao = input('Você ainda tem amigos? s/n: ')

    if sim_nao == 's':

        nome = input('Qual seu nome: ')
        numero_fav = input('Qual seu numero favorito? ')

        amigos[nome] = numero_fav
        
    else: amigostrue = False
else: print(amigos)

 





