import random

contador = 0
while True:
    number = int(input('Digite o inteiro: '))
    nRandom = random.randint(1, 10)
    if number == nRandom:
        print('Parabens! Você acertou! \n')
        break
    else:
        print('Errou! Tente novamente. \n')
    contador += 1
print(f'Você tentou {contador} vezes antes de acertar.')
