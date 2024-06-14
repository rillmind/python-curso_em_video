soma = 0
contador = 0
while True:
    numbers = int(input('Digite um inteiro: '))
    if numbers == 999:
        break
    soma += numbers
    contador += 1
print(f'Foram contabilizados {contador} números e a soma deles é = {soma}')