import time

for count in range(5):
    print(f'Cycle number {count + 1}')
    print('RED')
    time.sleep(4)
    print('RED-YELLOW')
    time.sleep(2)
    print('CLEAR')
    time.sleep(0.3)
    print('GREEN')
    time.sleep(5)
