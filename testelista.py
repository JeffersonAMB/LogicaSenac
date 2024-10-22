#criando lista
lista_animais = ['gato','cachorrro','papagaio','cobra','pássaro']
for animais in lista_animais:
    print(animais)

#operações na lista
lista_numeros = [1,2,3,4,5]
lista2 = [x* 2 for x in lista_numeros]
print(lista2)

#adicinando a lista 'append'
lista = [1,2,3,4,]
lista.append(500)
print(lista)

lista = ['gato','cachorrro','papagaio','cobra','pássaro']
lista.append('macaco')
print(lista)

#acessar elemento da lista
lista = ['gato','cachorrro','papagaio','cobra','pássaro']
print(lista[-1])

#substituindo na lista
lista3 = ['gato','cachorrro','papagaio','cobra','pássaro']
lista3[1] = 'macaco'
print(lista3)

#removendo da lista 'del'
lista3 = ['gato','cachorrro','papagaio','cobra','pássaro']
del lista3[1]
print(lista3)

#buscar na lista 'in'
lista3 = ['gato','cachorrro','papagaio','cobra','pássaro']
print('gato' in lista3)

#juntando listas 
lista_geral = lista + lista_numeros
print(lista_geral)

#inserindo a lista insert()
lista10 = ['gato','cachorrro','papagaio','cobra','pássaro']
lista10.insert(0,'macaco')
print(lista10)

#removendo com pop()
lista1 = [1,2,3,4]
elemento = lista1.pop()
print(lista1)
print(elemento)

#limpando a lista clear()
lista1 = [1,2,3,4]
lista1.clear()
print(lista1)

#encontrar posição index()
lista = ['gato','cachorrro','papagaio','cobra','pássaro']
indice = lista.index('gato')
print(indice)

#contando os itens da lista count()
lista = ['gato','cachorrro','papagaio','cobra','pássaro','gato']
listando = lista.count('gato')
print(listando)

#ordenar ou inverter listas sort()
lista_ordenar = ['gato','cachorrro','papagaio','cobra','pássaro','macaco','zebra']
lista_ordenar.sort()
print(lista_ordenar)

#'reverse'
lista_ordenar = ['gato','cachorrro','papagaio','cobra','pássaro','macaco','zebra']
lista_ordenar.reverse()
print(lista_ordenar)

#conjunto 'set'
lista_conjunto = ['gato','cachorrro','papagaio','cobra','pássaro','macaco','zebra''gato','gato']
lista_conjunto = list(set(lista_conjunto))
print(lista_conjunto)