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
            return('\n\033[0;31mUsuário interrompeu o programa!\033[m')  # SE TROCAR O 'RETURN' POR 'PRINT' NÃO FUNCIONA!
        else:
            if ok:
                break
    return value
        
def readFloat(n):
    ok = False
    value = 0
    while True:
        try:
            inteiro = float(input(n))
            if inteiro:
                value = float(inteiro)
                ok = True
        except ValueError:
            print('\033[0;31mERRO! Valor inválido!.\033[m')
        except KeyboardInterrupt:
            return('\n\033[0;31mUsuário interrompeu o programa!\033[m')  # SE TROCAR O 'RETURN' POR 'PRINT' NÃO FUNCIONA!
        if ok:
            break
    return value