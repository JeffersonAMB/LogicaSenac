#criando tuplas criada entre '()'
tupla = ('gato','cachorrro','papagaio','cobra','pássaro')
print(tupla)

#acessando itens
print(tupla[:1])
print(tupla[0:2])
print(tupla[-1])
print(tupla[:])

#imprimir o item
tupla = ('gato','cachorrro','papagaio','cobra','pássaro')
for x in tupla:
    print(x)

#checando valores se está na tupla
tupla = ('gato','cachorrro','papagaio','cobra','pássaro')
print('macaco' in tupla)

#tamanho da tupla
tupla = ('gato','cachorrro','papagaio','cobra','pássaro')
print(len(tupla))

#deletando da tupla
tupla = ('gato','cachorrro','papagaio','cobra','pássaro')
del tupla

#contruindo automaticamente
tupla = tuple(x for x in range(0,30,2))
print(tupla)

#método "count"
tupla = ('gato','cachorrro','papagaio','cobra','pássaro','gato')
print(tupla.count('gato'))

#método index
tupla = ('gato','cachorrro','papagaio','cobra','pássaro','gato')
print(tupla.index('gato'))