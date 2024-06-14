times = (
    'Athletico-PR', 'Bahia', 'Flamengo', 'Botafogo', 'São Paulo',
    'Cruzeiro', 'Atlético-MG', 'Bragantino', 'Palmeiras', 'Internacional',
    'Fortaleza','Grêmio', 'Vasco da Gama', 'Criciúma', 'Juventude',
    'Corinthians', 'Fluminense', 'EC Vitótia', 'Atlético-GO','Cuiabá'
)

print('')
print(f'Os 5 primeiros colocados são: ')
for c in times[:5]:
    print(c)
print(' ')
print(f'Os 4 últimos colocados são: ')
for c in times[16:]:
    print(c)
print(' ')
print(f'Os times em ordem alfabética: ')
for c in sorted(times):
    print(c)
print(' ')
print(f'Chapecoense não está na série A!')
