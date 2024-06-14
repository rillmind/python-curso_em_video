maiorIdade = 0
menorIdade = 0
for c in range(1, 8):
    ano = int(input(f'Ano de nascimento da pessoa {c}: '))
    if 2024 - ano >= 18:
        maiorIdade += 1
    elif 2024 - ano < 18:
        menorIdade += 1
print(f'{maiorIdade} pessoas são maiores de idade')
print(f'{menorIdade} pessoas são menores de idade')
