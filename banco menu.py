menu = '''

[d] depositar
[s] sacar
[e] extrato
[q] sair

=>'''

saldo = float()
limite = 500
extrato = (str())
numero_de_saques = 0
LIMITE_SAQUES = 3

while True:

    opicao = input(menu)

    if opicao == 'd':

        deposito = float(input('Digite o valor do deposito:'))

        if deposito > 0:
            saldo += deposito
            extrato += f'deposito: R${deposito:.2f}\n'
            print(f'deposito de R${deposito:.2f} efetuado com sucesso!\n')
        else:
            print('Falha! Valor inválido!')

    elif opicao == 's':

        saque = float(input('Digite o valor do saque:'))

        excedeu_saldo = saque > saldo
        excedeu_limite = saque > limite
        excedeu_saques = numero_de_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print('Saldo insuficiente!')
        elif excedeu_limite:
            print('Limite excedido!')
        elif excedeu_saques:
            print('Limite de saques excedido!')
        elif saque > 0:
            saldo -= saque
            extrato += f'Saque de R${saque:.2f}\n'
            numero_de_saques += 1
            print(f'Saque de R${saque:.2f} efetuado com sucesso!\n')
        else:
            print('Falha! Valor inválido!')

    elif opicao == 'e':
        print('\n############# extrato #############')
        print('Não foram realizadas movimentações!' if not extrato else extrato)
        print(f'\nSaldo igual: R${saldo:.2f}')
        print('\n##################################')

    elif opicao == 'q':
        break
    else:
        print('Operação inválida, por favor selecione novamente a operação desejada.')
