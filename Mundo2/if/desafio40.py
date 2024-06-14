grade1 = float(input('enter the first grade: '))
grade2 = float(input('enter the second grade: '))

average = (grade1 + grade2) / 2

if average < 5:
    print('Flunked')
elif 5 < average < 6.9:
    print('Remedial')
elif average > 7:
    print('Passed')
