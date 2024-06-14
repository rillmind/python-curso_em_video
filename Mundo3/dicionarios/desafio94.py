dicionario = {}
mulheres = []
pessoas = []
majors = []
idades = 0

while True:
    dicionario['nome'] = str(input('Nome: '))
    dicionario['idade'] = int(input('Idade: '))
    dicionario['sexo'] = str(input('Sexo: ')).strip().upper()[0]
    idades += dicionario['idade']
    pessoas.append(dicionario.copy())
    if dicionario['sexo'] == 'F':
        mulheres.append(dicionario.copy())
    dicionario.clear()
    
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break

for c2 in range(0, len(pessoas)):
    if pessoas[c2]['idade'] > (idades / len(pessoas)):
        majors.append(pessoas[c2].copy())
    
print('-=-' * 20)
print(f' - Quantidade de pessoas cadastradas: {len(pessoas)}.')
print(f' - Média de idade do grupo: {idades / len(pessoas):.1f}.')
print(f' - As mulheres cadastradas foram: ', end='')
for c3 in range(0, len(mulheres)):
    print(f'{mulheres[c3]['nome']}', end=' ')
print(f'\nPessoas com idade acima da média: ', end='')
for c4 in range(0, len(majors)):
    print(f'{majors[c4]['nome']}', end=' ')
print()
print('-=-' * 20)
    