numbers = list()

maior = 0
menor = 0

for c in range(0, 5):
    numbers.append(int(input('Digite um valor: ')))

    if c == 0:
        maior = menor = numbers[c]
    else:
        if numbers[c] > maior:
            maior = numbers[c]
        if numbers[c] < menor:
            menor = numbers[c]

print(f'\nO maior valor foi {maior} e ele está nas posições: ', end='')
for co in range(0, len(numbers)):
    if numbers[co] == maior:
        print(co, end='... ')

print(f'\nO menor valor foi {menor} e ele está nas posições: ', end='')
for con in range(0, len(numbers)):
    if numbers[con] == menor:
        print(con, end='... ')
