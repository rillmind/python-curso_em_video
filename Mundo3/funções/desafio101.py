def voto(ano):
    resultado = 2024 - ano
    if 65 >= resultado >= 18:
        return f'com {resultado} anos o voto é OBRIGATÓRIO!'
    elif 18 > resultado >= 16 or resultado > 65:
        return f'com {resultado} anos o voto é FACULTATIVO!'
    else:
        return f'com {resultado} não pode votar!'
    
ano = int(input('Ano de nascimento: '))
print(voto(ano))