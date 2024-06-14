aluno = {}

aluno['nome'] = str(input('Nome: '))
aluno['media'] = float(input('Média: '))

print(f'Nome do aluno: {aluno["nome"]}')
print(f'Média do aluno: {aluno["media"]}')
if aluno['media'] < 7:
    print('Reprovado.')
else:
    print('Aprovado!')
