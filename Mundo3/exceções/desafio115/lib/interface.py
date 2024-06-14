def line(tamanho = 40):
    print('-' * tamanho)
    
def header(tittle):
    line()
    print(tittle.center(40))
    line()
    
def readInt(n):
    ok = False
    value = 0
    while True:
        try:
            inteiro = int(input(n))
            if inteiro:
                value = int(inteiro)
                ok = True
        except ValueError:
            print('\033[0;31mERRO! Valor inválido!.\033[m')
        except KeyboardInterrupt:
            print('\n\033[0;31mSaída inválida. Digite 3!\033[m')
            return 0
        else:
            if ok:
                break
    return value
    
def menu(list):
    header('Main Menu')
    for c in range(0, len(list)):
        print(f'\033[33m{c + 1}\033[m - \033[34m{list[c]}\033[m')
    line()
    option = readInt('\033[32mSua Opção: \033[m')
    line()
    return option