def ficha(nome='<desconhecido>', gols=0):
    return(f'O jogador {nome} fez ({gols}) gols!')

nome = str(input('Nome: '))
gols = str(input('Gols: '))

if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0
    
if nome.strip() == '':
    print(ficha(gols=gols))
else:
    print(ficha(nome, gols))