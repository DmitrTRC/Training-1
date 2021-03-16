import time

for x in range(4):
    print(f'Cycle number {x + 1}')
    print('RED')
    time.sleep(4)
    print('RED-YELLOW')
    time.sleep(2)
    print('CLEAR')
    time.sleep(0.3)
    print('GREEN')
    time.sleep(5)
