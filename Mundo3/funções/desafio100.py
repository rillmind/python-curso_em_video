from random import randint

numbers = []

def sorteia():
    for c in range(0, 5):
        numbers.append(randint(0, 9))
    print(numbers)
    
def somaPar():
    soma = 0
    for c in numbers:
        if c % 2 == 0:
            soma += c
    print(soma)
    
sorteia()
somaPar()