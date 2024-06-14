valores = list()
continuar = ' '

while True:
    valores.append(int(input('Digite um valor: ')))
    
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if continuar in 'N':
        break
    
print(f'A quantidade de números digitados foi: {len(valores)}.')
valores.sort(reverse=True)
print(f'A lista em ordem decrescente: {valores}')
if 5 in valores:
    print('O valor 5 foi digitado!')
else:
    print('O valor 5 não foi digitado!')
