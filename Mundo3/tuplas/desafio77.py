x = (
    'alberto',
    'arroz',
    'feijoada',
    'abacate',
    'alicate',
    'franzino',
    'feio'
)

for c in x:
    print(f'\n{f'Na palavra "{c}" temos:':<30} ', end='')
    for con in c:
        if con in 'aeiou':
            print(con, end='')
