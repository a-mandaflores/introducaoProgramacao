saldo = int(input('Qual o seu saldo: '))
debito =  int(input('Qual seus debitos: '))
credito = int(input('Qual seu crédito: '))

saldo_atual = saldo - debito + credito

print(saldo_atual)

if saldo_atual > 0:
    print('Saldo positivo')
else:
    print('Você esta quebrado')