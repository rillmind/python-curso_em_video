def fatorial(n, show=False):
    for c in range(n -1, 0, -1):
        if show == False:
            n *= c
        else:
            if show == True:
                print(f'{n} x {c} = ', end='')
                n *= c
    print(n)
                
fatorial(5, True)
# fatorial(5)