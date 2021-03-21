import math

"""
Напечатать все делители числа
"""
number = int(input('The number -> '))
dividers = []
for item in range(1, number + 1):
    if not number % item:
        dividers.append(item)
print(f'Number of dividers : {len(dividers)} , Dividers: {dividers}')

# Alternative

count = 0
for item in range(1, number + 1):
    if not number % item:
        count += 1
        print(item, end=', ')
print(f'Total : {count}')


def get_dividers(num):
    div_arr = []
    for n in range(1, num + 1):
        if not num % n:
            div_arr.append(n)
    return div_arr


result = get_dividers(number)
print(result, len(result))
