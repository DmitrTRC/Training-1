for i in range(5):

    light = input('Enter traffic light color -> ').lower()

    if light == 'red':
        print('STOP!')
    elif light == 'yellow':
        print('ATTENTION!')
    elif light == 'green':
        print('GO!')
    else:
        print('TRAFFIC LIGHT IS WRONG!')
