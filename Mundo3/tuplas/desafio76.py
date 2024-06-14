listagem = (
    'Copo', 10.90,
    'Prato', 20,
    'Garfo', 2.50,
    'Faca', 2,
    'Colher', 3,
    'Tábua', 19.50,
)

print('-' * 30)
print(f'{'Listagem de preços':^30}')
print('-' * 30)
for c in range(0, len(listagem)):
    if c % 2 == 0:
        print(f'{listagem[c]:.<20}', end=' ')
    else:
        print(f'R${listagem[c]:>6.2f}')
print('-' * 30)
