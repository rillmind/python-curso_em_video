idades = 0
olderName = ''
minor20 = 0
for c in range(1, 5):
    nome = str(input(f'nome da {c}° pessoa: ')).strip()
    idade = int(input(f'idade da {c}° pessoa: '))
    sexo = str(input(f'sexo da {c}° pessoa [M/F]: ')).strip()
    idades += idade
    if c == 1 and sexo in 'Mm':
        older = idade
    else:
        if idade > older and sexo in 'Mm':
            olderName = nome
    if sexo in 'Ff' and idade < 20:
        minor20 += 1
    
mediaIdades = idades / 4

print('')
print(f'A média das idades do grupo é {mediaIdades}.')
print(f'O homem mais velho se chama {nome}.')
print(f'Ao todo são {minor20} mulheres com menos de 20 anos.')
