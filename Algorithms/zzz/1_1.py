a = int(input('a = '))
b = int(input('b = '))


def nsd(a, b):
    while a * b != 0:
        if a >= b:
            a = a % b
        else:
            b = b % a
    return a + b

def nsk(a, b):
    return a * b // nsd(a, b)


print(nsd(a, b))

print(nsk(a, b))