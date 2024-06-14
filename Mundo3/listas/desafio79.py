valores = list()

while True:
    valor = int(input('Digite um valor: '))
    if valor not in valores:
        valores.append(valor)
    else:
        print('Valor repetido. Não vou adicionar...')
    continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if continuar in 'N':
        break
        
valores.sort()
print('-='*20)
print(f'Você digitou os valores {valores}')