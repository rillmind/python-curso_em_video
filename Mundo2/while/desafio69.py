majors = 0
men = 0
minors = 0
while True:
    sexo = ' '
    continuar = ' '
    nome = str(input('Digite seu nome: '))
    idade = int(input('Digite sua idade: '))
    while sexo not in 'MF':
        sexo = str(input('Digite seu sexo: [M/F] ')).strip().upper()[0]
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if idade > 18:
        majors += 1
    if sexo == 'M':
        men += 1
    if sexo == 'F' and idade < 20:
        minors += 1
    if continuar == 'S':
        continue
    if continuar == 'N':
        break
        
print(f'{majors} pessoas são maiores de 18 anos.')
print(f'{men} homens foram cadastrados.')
print(f'{minors} mulheres tem menos de 20 anos.')