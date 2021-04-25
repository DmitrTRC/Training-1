def swap1(a, b):
    c = a
    a = b
    b = c
    return a, b


def swap2(a, b):
    a, b = b, a
    return a, b


c = 10
e = 40
print(c, e)
c, e = swap2(c, e)
print(c, e)
