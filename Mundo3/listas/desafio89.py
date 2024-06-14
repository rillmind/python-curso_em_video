alunos = []

while True:
    nome = str(input('Nome do aluno: '))
    nota1 = float(input('1° nota do aluno: '))
    nota2 = float(input('2° nota do aluno: '))
    media = (nota1 + nota2) / 2
    alunos.append([nome, [nota1, nota2], media])
    
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break

for c in range(0, len(alunos)):
    print(f'{c:<2} {alunos[c][0]:^7} {alunos[c][2]:>2}')
    
while True:
    aluno = int(input('\nDeseja ver a nota de qual aluno? '))
    if aluno == 99:
        break
    print(f'\nA notas de {alunos[aluno][0]} foram: {alunos[aluno][1]}\n')
