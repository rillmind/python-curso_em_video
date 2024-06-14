valores = list()

for c1 in range(0, 5):
    valor = int(input('Digite um valor: '))
    if c1 == 0 or valor > valores[-1]:
        valores.append(valor)
        print('Adicionado ao final da lista!')
    else:
        c2 = 0
        while c2 < len(valores):
            if valor <= valores[c2]:
                valores.insert(c2, valor)
                print(f'Adicionado na posição {c2} da lista!')
                break
            c2 += 1
print(f'Os valroes digitados em ordem fora: {valores}')