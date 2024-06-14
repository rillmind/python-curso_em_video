soma = 0
maior = 0
menor = 0
contador = 1
while True:
    numbers = int(input('Digite um inteiro: '))
    soma += numbers
    if contador == 1:
        maior = numbers
        menor = numbers
    else:
        if numbers > maior:
            maior = numbers
        if numbers < menor:
            menor = numbers
    contador += 1
    continuar = str(input('Deseja continuar? [S/N]')).upper()
    if continuar == 'S':
        continue
    elif continuar == 'N':
        break
print(f'A média entre os valores foi de: {soma / contador}')
print(f'E o maior valor foi: {maior}')
print(f'E o menor valor foi: {menor}')