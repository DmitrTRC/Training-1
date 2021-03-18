while True:
    print('Hello')
    age = int(input('Enter your age -> '))
    answer = input('Do you want to continue? y/n -> ')
    if (answer == 'y' or answer == 'Y') and age >= 16:
        print(age)
        continue
    else:
        break

print('good luck!')
