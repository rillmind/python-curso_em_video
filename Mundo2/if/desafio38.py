value1 = int(input('Enter the first value: '))
value2 = int(input('Enter the second value: '))

if value1 > value2:
    print('The first value is bigger than the second one.')
elif value2 > value1:
    print('The second value is bigger than the first one.')
elif value1 == value2:
    print('They have the same value.')
