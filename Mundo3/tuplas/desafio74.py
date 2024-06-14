from random import randint

rand1 = randint(1, 10)
rand2 = randint(1, 10)
rand3 = randint(1, 10)
rand4 = randint(1, 10)
rand5 = randint(1, 10)

menor = 0
maior = 0
tupla = (rand1, rand2, rand3, rand4, rand5)
print('Os valores sorteados foram: ', end='')
for c in range(0, len(tupla)):
    print(tupla[c], end=' ')
    if c == 0:
        maior = tupla[c]
        menor = tupla[c]
    elif tupla[c] > maior:
        maior = tupla[c]
    elif tupla[c] < menor:
        menor = tupla[c]
print('\n')
print(f'O maior valor foi: {maior}')
print(f'O menor valor foi: {menor}')
