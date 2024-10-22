impares = 0
pares = 0
for x in range(10):
    n = int(input('digite um numero:'))
    if n %2 == 1:
        impares +=1
    else:
        pares +=1
print(pares)
print(impares)
