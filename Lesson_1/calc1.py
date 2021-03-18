while True:
    number_1 = float(input('Enter number 1 -> '))
    number_2 = float(input('Enter number 2 -> '))
    operator = input('Enter operator -> ')
    result = None
    if operator == '+':
        result = number_1 + number_2
    elif operator == '-':
        result = number_1 - number_2
    elif operator == '*':
        result = number_1 * number_2
    elif operator == '/':
        result = number_1 / number_2
    else:
        print('Unknown operator')

    if result:
        print(f'Result of operation: {result}')
    else:
        print('Can not calculate this expression')
    answer = input('Do you want to continue ? y/n -> ')
    if answer == 'n' or answer == 'N':
        break
