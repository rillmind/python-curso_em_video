number = int(input('Qual tabuada deseja saber? '))
print('')
contador = 1
while True:
    if number <= 0:
        break
    print(f'{number} x {contador} = {number * contador}')
    contador += 1
    if contador == 10:
        print('')
        number = int(input('Qual tabuada deseja saber? '))
        print('')
        contador = 1
        continue
    