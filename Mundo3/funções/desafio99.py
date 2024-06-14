from time import sleep

def maior(*n):
    c = 0
    maior = 0
    print('Analisando valores: ', end='')
    for valor in n:
        print(valor, end=' ', flush=True)
        sleep(0.5)
        
        if c == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        c += 1
    print(f'O maior valor é {maior}')
    

maior(1, 2, 3, 4, 5)
maior(5, 6, 7, 10, 3, 2)
maior()
maior(7)