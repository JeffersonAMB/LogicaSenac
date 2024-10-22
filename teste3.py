vari1 = int(input('digite o valor:'))
vari2 = int(input('digite o valor:'))
carac = input('digite o caractere:')

match carac:
    case '+':
        print(vari1 + vari2) 
    case '-':
        print(vari1 - vari2)
    case '*':
        print(vari1 * vari2)  
    case '/':  
        print(vari1 / vari2)
    case _:  
        print('operação invalida!')