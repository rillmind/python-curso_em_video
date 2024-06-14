housePrice = float(input('Enter the value of the house: '))
salary = float(input('Enter the value of your salary: '))
yersCount = float(input('How many years you will pay the house? '))

installment = housePrice / yersCount / 12

thirtyPorcent = salary * 0.3

if installment >= thirtyPorcent:
    print('Loan denied!')
else:
    print('Loan approved!')
