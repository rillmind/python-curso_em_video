pessoa = {}

pessoa['nome'] = str(input('Digite seu nome: '))
pessoa['idade'] = 2024 - int(input('Digite seu ano de nascimento: '))
pessoa['carteira de trabalho'] = int(input('Digite sua carteira de trabalho: '))
if pessoa['carteira de trabalho'] != 0:
    pessoa['ano de contratação'] = int(input('Digite o ano de contratação: '))
    pessoa['salário'] = float(input('Digite seu salário: '))

print(f'Nome da pessoa: {pessoa["nome"]}')
print(f'Idade da pessoa: {pessoa["idade"]}')
print(f'CTPS da pessoa: {pessoa["carteira de trabalho"]}')
if pessoa['carteira de trabalho'] != 0:
    print(f'Ano de contratação: {pessoa["ano de contratação"]}')
    print(f'Salário: {pessoa["salário"]}')
    print(f'Essa pessoa irá se aposentar com: {pessoa["idade"] + 35}')
