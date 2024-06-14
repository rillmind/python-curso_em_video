numbers = (
    int(input('Digite um inteiro: ')),
    int(input('Digite um inteiro: ')),
    int(input('Digite um inteiro: ')),
    int(input('Digite um inteiro: '))
)

print(f'O número 9 apareceu {numbers.count(9)} vezes.')
if 3 in numbers:
    print(f'O número 3 foi digitado na posição {numbers.index(3) + 1}°.')
else:
    print('O número 3 não foi digitado em nenhuma posição.', end='')
print('Os números pares foram: ', end='')
for c in numbers:
    if c % 2 == 0:
        print(c, end=' ')
