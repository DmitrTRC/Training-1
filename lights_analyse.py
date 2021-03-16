color = None
while color != 'quit':
    color = input('Enter traffic light color -> ')
    color = color.lower()
    if color == 'red':
        print('STOP!')
    elif color == 'yellow':
        print('WARNING!')
    elif color == 'green':
        print('GO!')
    else:
        print('Wrong color!')
