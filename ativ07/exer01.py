#Use um dicionário para armazenar informações sobre uma pessoa que você conheça. Armazene seu
#primeiro nome, o sobrenome, a idade e a cidade em que ela vive. Você deverá ter chaves como
#primeiro_nome, sobrenome, idade, e cidade. Por fim, mostre cada informação armazenada em seu
#dicionário.

print('Estou funcionando')

infos = {
    'Primeiro nome': '',
    'Sobrenome': '',
    'Idade': '',
    'Cidade': ''
}

infos['Primeiro nome'] = input('Qual seu primeiro nome? ')
infos['Sobrenome'] = input('Qual o seu sobrenome? ')
infos['Idade'] = int(input('Qual a sua idade? '))
infos['Cidade'] = input('Em que cidade você vive? ')

print(infos)