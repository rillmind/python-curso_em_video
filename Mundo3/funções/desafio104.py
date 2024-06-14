def readInt(n):
    ok = False
    value = 0
    while True:
        inteiro = str(input(n))
        if inteiro.isnumeric():
            value = int(inteiro)
            ok = True
        else:
            print('\033[0;31mERRO! Digite um número inteiro válido.\033[m')
        if ok:
            break
    return value
        
inteiro = readInt('Digite um inteiro: ')
print(inteiro)