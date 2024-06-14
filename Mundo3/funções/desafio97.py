def escreva(txt):
    print('~' * len(txt))
    print(f'{txt:^}')
    print('~' * len(txt))
    
escreva(txt=str(input('Digite um texto qualquer: ')))