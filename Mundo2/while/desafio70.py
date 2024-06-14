total = 0
contador1000 = 0
menorPreco = 0
menorNome = ' '
contador = 1
while True:
    nome = str(input('Digite o nome do produto: '))
    preco = float(input('Digite o preco do produto: '))
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break
    if preco > 1000:
        contador1000 += 1
    if contador == 1:
        menorPreco = preco
        menorNome = nome
    elif preco < menorPreco:
        menorPreco = preco
        menorNome = nome
    total += preco
print(f'O total gasto na compra foi: R${total}!')
print(f'O total de produtos custam mais de R$1000.00 é: {contador1000}!')
print(f'O nome do produto mais barato é {menorNome} e custa R${menorPreco:.2f}!')