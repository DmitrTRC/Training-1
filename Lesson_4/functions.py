def summa(a, b=10):
    return a + b


def print_user_name(name, lastname, age, x=','):
    user_name = x.join([name, lastname, age])
    print(user_name)


contacts = [
    'Dmitry',
    'Margo',
    'Natasha',
    'Anna',
    'Sveta'
]

# x = int(input('x -> '))
# y = int(input('y -> '))
# print('Before call summa')
# c = summa(x, y)
# print('After call')
# print(c)
print_user_name('Dmitry', 'Morozov', '45', x=' *** ')
