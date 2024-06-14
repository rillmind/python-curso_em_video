from moedas import aumentar, diminuir, dobro, metade

n = float(input('Digite o preço: R$'))

print(f'A metade de {n} é {metade(n)}')
print(f'O dobro de {n} é {dobro(n)}')
print(f'Aumentando 10% em {n} temos {aumentar(n, 10)}')
print(f'Diminuindo 13% em {n} temos {diminuir(n, 13)}')