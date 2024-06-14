from random import randint
from time import sleep

lista1 = []
lista2 = []

print('-' * 30)
print(f'{'Jogo da MEGA SENA':^30}')
print('-' * 30)

quantidade = int(input('Quantas vezes deseja sortear: '))
print('-' * 30)
c = 1
while c <= quantidade:
    c2 = 0
    while True:
        randomNumber = randint(1, 60)
        if randomNumber not in lista2:
            lista2.append(randomNumber)
            c2 += 1
        if c2 >= 6:
            break
    lista2.sort()
    lista1.append(lista2[:])
    lista2.clear()
    c += 1
        
sleep(1)
for c in range(0, len(lista1)):
    print(f'Jogo {c + 1}: {lista1[c]}')
    sleep(1)
