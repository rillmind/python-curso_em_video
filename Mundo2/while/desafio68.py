from random import randint

victorys = 0
while True:
    print('')
    jogador = int(input('[1] Pedra, [2]Papel ou [3]Tesoura? '))
    print('')
    computador = randint(1, 4)
    if jogador == computador:
        print('Empate!')
        continue
    elif jogador == 1 and computador == 3:
        print('Ganhou!')
        victorys += 1
        continue
    elif jogador == 2 and computador == 1:
        print('Ganhou!')
        victorys += 1
        continue
    elif jogador == 3 and computador == 2:
        print('Ganhou!')
        victorys += 1
        continue
    else:
        print(f'Você perdeu! o total de vitórias consecutivas foi: {victorys}')
        break
        