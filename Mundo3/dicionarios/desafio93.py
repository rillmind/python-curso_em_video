jogador = {}
gols = []
soma = 0

jogador['nome'] = str(input('Digite o nome do jogador: '))
jogador['partidas'] = int(input(f'Digite quantas partidas {jogador["nome"]} jogou: '))

for c in range(0, jogador['partidas']):
    gol = int(input(f'Quantos gols ele fez no {c + 1}° jogo? '))
    gols.append(gol)
    
jogador['gols'] = gols[:]

for c2 in gols:
    soma += c2
    
jogador['total de gols'] = soma

print('-' * 20)
print(f'Nome do jogador: {jogador["nome"]}')
print(f'Os gols do jogador: {jogador["gols"]}')
print(f'O total de gols no campeonato: {jogador["total de gols"]}')
print('-' * 20)

print(f'O jogador {jogador["nome"]} jogou {jogador["partidas"]} partidas.')
for c3 in range(0, len(jogador['gols'])):
    print(f'Na {c3 + 1}° partida {jogador["nome"]} fez {jogador["gols"][c3]} gols.')
print(f'Um total de {jogador["total de gols"]} de gols.')