while(True):
    sexo = str(input(f'Digite seu sexo [M/F]: '))
    if sexo in 'MF':
        break
    else:
        print('Digite corretamente!')