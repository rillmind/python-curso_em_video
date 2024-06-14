while True:
    number1 = int(input('Digite o primeiro número: '))
    number2 = int(input('Digite o segundo número: '))
    print('')
    print(' Você deseja: ')
    print(' [1] Somar. ')
    print(' [2] Multiplicar.')
    print(' [3] Maior.')
    print(' [4] Novos valores.')
    print(' [5] Sair.\n')
    escolha = int(input('Escolha: '))
    print('')
    
    if escolha == 1:
        print(f'A soma dos valores é = {number1 + number2}\n')
        continue
    elif escolha == 2:
        print(f'A multiplicação dos valores é = {number1 * number2}\n')
        continue
    elif escolha == 3:
        if number1 > number2:
            print(f'O maior valor é = {number1}\n')
            continue
        if number1 < number2:
            print(f'O maior valor é = {number1}\n')
            continue
        if number1 == number2:
            print('Os valores são iguais\n')
    elif escolha == 4:
        continue
    elif escolha == 5:
        print('Saindo...\n')
        break
            