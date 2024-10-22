#manipulação de 'str'

# operadores '+' ou '*'
numero = 5
print('o numero é:' * numero)

#operardor in
frase = 'eu Não sei disso'
result = 'eu' in frase
print(result) #diferencia maiuscula
print('não' in frase.lower()) #não diferencia maiuscula de minuscula

#função 'Len()'
frase2 = 'sou papai'
quantidade = len(frase2)
print(f'a frase tem {quantidade} caractere') #conta a quantidade de caractere

#função 'slicing()'
frase3 = 'me tornei papai ontem'
print(frase3[:5]) #imprime apenas a contagem

#função 'capitalize()' tranforma a primeira em maiuscula E O RESTO EM MINUSCULA
frase3 = 'Me tornei papai ONTEM'
print(frase3.capitalize())

#função 'title()'
frase3 = 'Me tornei papai ONTEM'
print(frase3.title())

#função 'upper()' e 'lower()'
frase3 = 'Me tornei papai ONTEM'
print(frase3.upper())
print(frase3.lower())

#função count() usada para contar a posição do caractere
frase3 = 'Me tornei papai ONTEM'
print(frase3.count('me')) #não só palavras como letas

#função 'split()' 
frase3 = 'Me tornei papai, ONTEM'
print(frase3.split()) #separa cada caractere
print(frase3.split(','))#a virgula e separa

#função endswith() e startswtih
#endswith se termina com '()'
frase3 = 'Me tornei papai, ONTEM'
verif = frase3.endswith('ONTEM')
print(verif)
#startswith se começa com '()'
frase3 = 'Me tornei papai, ONTEM'
verif = frase3.startswith('Me')
print(verif)

#função find() e replace()
frase3 = 'Me tornei papai, ONTEM'
verif = frase3.find('me') #retorna a posição(indice)
print(verif)

frase3 = 'Me tornei papai, ONTEM'
verif = frase3.replace('ONTEM','anteontem')# substitui
print(verif)

