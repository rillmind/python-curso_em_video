maior = 0
menor = 0
for c in range(1, 6, 1):
    peso = float(input(f'peso da {c}° pessoa: '))
    if c == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f'O maior peso lido foi de {maior}Kg')
print(f'O menor peso lido foi de {menor}Kg')