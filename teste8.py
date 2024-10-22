saldo = 0
opcoes = 's'
emprestimo = 500
while opcoes == 's':
    print('digite 1 para saldo!')
    print('digite 2 para saque!')
    print('digite 3 para deposito!')
    print('digite 4 para falar com atendente!')
    print('digite 5 para emprestimos!')
    print('digite 0 para encerrar!')
    opcao = int(input('digite uma das opções:'))
    match opcao:
        case 1:
            print('seu saldo é:', saldo)
        
        case 2:
            saque = int(input('digite o valor para saque:'))
            if saque > saldo:
                print('saldo insuficiente!')
            else:
                saldo -= saque
                print('aguarde a saida das notas!')
        
        case 3:
            deposito = int(input('digite o valor para depositar:'))
            saldo += deposito
            print(f'saldo atual:', saldo)
        
        case 4:
            input('aguarde, você será encaminhado para um de nossos atendentes!')
        
        case 5:
            emprestimo_cliente = int(input('digite o valor para emprestimo:'))
            if emprestimo_cliente > emprestimo:
                print('valor acima do limite!')
            
            elif emprestimo_cliente < emprestimo:
                emprestimo -= emprestimo_cliente
                saldo += emprestimo_cliente
                print('saldo atual:',saldo)

        case 0:
            print('certo, encerramos!')