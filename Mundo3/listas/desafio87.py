lista = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
sPares = 0
soma = 0
maior = 0

for c1 in range(0, 3):
    for c2 in range(0, 3):
        lista[c1][c2] = int(input('Digite um valor: '))
        
print()
        
for c1 in range(0, 3):
    for c2 in range(0, 3):
        print(f'[{lista[c1][c2]:^3}]', end=' ')
    print()
    
for c1 in range(0, 3):
    for c2 in range(0, 3):
        if lista[c1][c2] % 2 == 0:
            sPares += lista[c1][c2]
            
for c1 in range(2, 3):
    for c2 in range(0, 3):
        soma += lista[c1][c2]
        
for c1 in range(1,2):
    for c2 in range(0, 3):
        if c2 == 0:
            maior = lista[c1][c2]
        elif lista[c1][c2] > maior:
            maior = lista[c1][c2]


print(f'\nA soma dos valores pares é {sPares}')
print(f'A soma dos valores da terceira coluna é {soma}')
print(f'O maior valor da segunda linha é {maior}')