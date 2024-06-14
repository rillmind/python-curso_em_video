age = int(input('which year did you born? '))
j = 2024 - age

if j < 18:
    print('The time to enlist in the army will come.')
    print(f'There are {(j - 18) * (-1)} years left to enlist.')
elif j == 18:
    print('You have to enlist in the army this year')
elif j > 18:
    print('The time you enlist in the army has passed.')
    print(f'{j - 18} Years have passed.')
