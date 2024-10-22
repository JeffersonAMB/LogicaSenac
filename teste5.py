resposta = input('você quer calcular? "s" ou "n":')
contador = 's'

while resposta == 's':
    n1 = int(input('digite numero:'))
    carac = input('caractere:')
    n2 = int(input('digite outro numero:'))
    match carac:
        case '+':
            print(n1 + n2)
        case '-':
            print(n1 - n2)
        case '*':
            print(n1 * n2)
        case '/':
            print(n1 / n2)
        case _:
            print('operação invalida!')
    resposta = input('deseja continuar? "s" ou "n":')
    if resposta == 'n':
        print('ok, finalizamos!')