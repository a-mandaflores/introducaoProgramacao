idade = int(float(input('Digite a sua idade: ')))

if idade > 18:
    print('Pode entrar na festa!')
elif idade > 15 and idade == 18:
    print('Não pode entrar')
else:
    print('Volta pra casa criança')


