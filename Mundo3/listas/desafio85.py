pares = list()
impares = list()
lista = [pares, impares]

for c1 in range(0, 7):
    valor = int(input('Digite um inteiro: '))
    if valor % 2 == 0:
        pares.append(valor)
    else:
        impares.append(valor)
        
pares.sort()
impares.sort()
print(f'Os valores Pares são: {pares}.')
print(f'Os valores Ímpares são: {impares}')