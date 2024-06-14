lista1 = []
maisP = 0
menosP = 0

while True:
    nome = str(input('Digite seu nome: '))
    peso = float(input('Digite seu peso: '))
    lista1 = [nome, peso]
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar: [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break

print(f'O total de pessoas cadastradas: {lista1}.')
# TO DO
