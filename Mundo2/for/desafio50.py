soma = 0
contador = 0
for c in range(1, 7, 1):
    contador += 1
    number = int(input(f'Digite o valor {contador, c} valores: '))
    if number % 2 == 0:
        soma += number
print(f'A soma dos números pares é {soma}')
