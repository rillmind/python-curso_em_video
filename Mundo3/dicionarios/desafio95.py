jogadores = []
jogador = {}
gols = []
soma = 0

while True:
    jogador['nome'] = str(input('Digite o nome do jogador: '))
    jogador['partidas'] = int(input(f'Digite quantas partidas {jogador["nome"]} jogou: '))

    for c in range(0, jogador['partidas']):
        gol = int(input(f'Quantos gols ele fez no {c + 1}° jogo? '))
        gols.append(gol)
        
    jogador['gols'] = gols[:]

    for c in gols:
        soma += c
        
    jogador['total de gols'] = soma
    
    jogadores.append(jogador.copy())
    jogador.clear()
    gols.clear()
    soma = 0
    
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break

print('-=-' * 13)
print(f'{'code':<5} {'nome':<12} {'gols'} {'total':>12}')
for c in range(0, len(jogadores)):
    print(f'{c + 1:<5} {jogadores[c]['nome']:<12} {jogadores[c]['gols']} {jogadores[c]['total de gols']:>6}')
print('-' * 39)

while True:
        qual = int(input('Mostrar dados de qual jogador? '))
        if qual == 999:
            break
        elif qual == len(jogadores):
            print('Jogador não foi cadastrado!')
        else:
            for c in range(0, len(jogadores)):
                if c == qual - 1:
                    print(f' - LEVANTAMENTO DO JOGADOR {jogadores[c]['nome']}: ')
                    for c2 in range(0, len(jogadores[c]['gols'])):
                        print(f'    No {c2 + 1}° jogo fez {jogadores[c]['gols'][c2]} gols.')
            
