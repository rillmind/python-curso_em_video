tudo = list()
pares = list()
impares = list()
continuar = ' '

while True:
    tudo.append(int(input('Digite um valor:  ')))
    
    while continuar not in 'SN':
        continuar = str(input('deseja continuar? [S/N]')).strip().upper()[0]
    if continuar in 'N':
        break

for c1 in tudo:
    if c1 % 2 == 0:
        pares.append(c1)
    else:
        impares.append(c1)
            
print('\nTodos os valores: ', end='')
for c2 in tudo:
    print(c2, end=' ')
print('\nValores pares: ', end='')
for c3 in pares:
    print(c3, end=' ')
print('\nValores Ímpares: ', end='')
for c4 in impares:
    print(c4, end=' ')
