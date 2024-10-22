saldo = 0
opcoes = 's'
emprestimo = 500
respostas = 'sim'

dicionario_clientes = {
       '9999': {'nome': 'Jefferson','usuario':'jefferson','senha': 123},
       '8888': {'nome': 'luyz','usuario': 'luyz', 'senha': 123}
       }

#1        
def saldo_atual():
            print('seu saldo é:', saldo)

#2
def saque():
    global saldo
    saque = int(input('digite o valor para saque:'))
    if saque > saldo:
                print('saldo insuficiente!')
    else:
                saldo -= saque
                print('aguarde a saida das notas!')
                print('saldo atual:', saldo)

#3
def deposito():
            global saldo 
            deposito = int(input('digite o valor para depositar:'))
            saldo += deposito
            print(f'saldo atual:', saldo)

#4     
def atendente():
            input('entre em contato no numero (83)9.1234-4567')
                
#5
def encerrar_conta():
       global dicionario_clientes
       encerrar = input('digite seu cpf:')
       del dicionario_clientes[encerrar]
       print('pronto! conta encerrada!')
       
#6
def emprestimos():
    global emprestimo
    global saldo
    emprestimo_cliente = int(input('digite um valor para sacar:'))
    emprestimo -= emprestimo_cliente
    saldo += emprestimo_cliente
    print('pronto, saldo em conta')
    print('saldo atual:', saldo) 

#0
def encerrar():
            print('certo, encerramos!')
            

#tela inicial
def iniciar(x):
    if x in dicionario_clientes:
        while opcoes == 's':        
            print('\ndigite 1 para saldo!')
            print('digite 2 para saque!')
            print('digite 3 para deposito!')
            print('digite 4 para falar com atendente!')
            print('digite 5 para encerrar conta')
            print('digite 6 para emprestimo!')
            print('digite 0 para encerrar atendimento!')
            opcao = int(input('\ndigite uma das opções:'))
            match opcao:
                case 1:
                    saldo_atual()
                case 2:
                    saque()
                case 3:
                    deposito()
                case 4:
                    atendente()
                case 5:
                    encerrar_conta()
                case 6:
                    emprestimos()
                case 0:
                    encerrar()
                    break
                case 10:
                        print(dicionario_clientes)
    else:
          adicionar_cliente()
        

#novo cliente
def adicionar_cliente():
    cpf = input('digite seu cpf:')
    nome = input('digite seu nome completo:')
    senha = input('crie uma senha:')
    senha_conf = len(senha)
    while int(senha_conf) < 6:
        senha_nova = input('senha invalia, crie uma senha com mais 6 digitos:')

        if int(len(senha_nova)) >=6:
                    senha_conf = senha_nova
                    usuario = nome.split()
                    login = usuario[0].capitalize()
                    dicionario_clientes[cpf] = {'nome': nome,'usuario': login , 'senha': senha}
                    print('pronto, cadastro finalizado')
                    print(f'seu login é: {login}')
    
    iniciar(cpf)
                    
#verificando dicionario
def verif_dicionario(x):

        if x in dicionario_clientes:
            iniciar(x)
        else:
            novo_cadastro = input('cpf não cadastrado! Deseja se tornar nosso cliente?')
            if novo_cadastro == respostas:
                adicionar_cliente()
            else:
                print('ok, encerramos')