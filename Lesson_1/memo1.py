i = 123
f = 13.2
s = 'Dmitry'
my_list = [1, 2, 3, 4, 5, 6]
my_dict = {
    'Dmitry': 1975,
    'Margo': 2009,
    'Tatiana': 1975,
}
contacts = ['Dmitry', 'Valya', 'Dmitry', 'Oleg', 'Viktor', 'Sergey', 'Valya']
my_set = set(contacts)
print(contacts)
print(my_set)

for number in my_list:
    print(number)
for name, date_birth in my_dict.items():
    print(name, date_birth)
for number in my_set:
    print(number)

number = int(input('Enter number -> '))
print(f'Integer number : {number}')
if number % 2 == 0:
    print('This is ODD number')
else:
    print('This is EVEN number')

if number < 0:
    print('Number is NEGATIVE')
else:
    if number > 0:
        print('Number is POSITIVE')
    else:
        print('Number is ZERO!')

i = 0
while i <= 10:
    print(f'Hello {i}', )
    i += 5  # i = i * 5

if number < 0:
    print('Number is NEGATIVE')
elif number > 0:
    print('Number is POSITIVE')
else:
    print('Number is ZERO!')

count = 0
while count < 1000:
    count += 1
    if count == 7:
        continue
    if count == 15:
        break
    print(f'{count=}')
print('Loop ended')
for i in range(10, 20, 2):
    print(i)
name = 'Dmitry'
for letter in name:
    print(letter, end='\n')

