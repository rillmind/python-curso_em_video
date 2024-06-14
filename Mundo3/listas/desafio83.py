parenteses = list()
quantidade = 0

parenteses.append(str(input('Digite uma expressão com "()": ')))

for c1 in parenteses:
    for c2 in c1:
        if c2 in '()':
            quantidade += 1

if quantidade % 2 == 0:
    print('Expressão válida!')
elif quantidade % 2 != 0:
    print('Expressão inválida!')
    
print(parenteses)