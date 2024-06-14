number = int(input('Digite um inteiro: '))
contador = number
fatorial = 1
while contador > 0:
    print(contador, end=' ')
    fatorial *= contador
    contador -= 1
    
print('')
print(f'O fatorial de {number} é {fatorial}')