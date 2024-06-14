soma = 0
contador = 0
while True:
    numbers = int(input('Digite um inteiro: '))
    soma += numbers
    contador += 1
    if numbers == 999:
        break

print(f'{contador} inteiros foram digitados e a soma deles é = {soma}')
