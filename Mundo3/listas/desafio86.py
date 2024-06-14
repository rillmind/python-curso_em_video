lista = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for c1 in range(0, 3):
    for c2 in range(0, 3):
        lista[c1][c2] = int(input('Digite um valor: '))
        
for c1 in range(0, 3):
    for c2 in range(0, 3):
        print(f'[{lista[c1][c2]:^3}]', end=' ')
    print()