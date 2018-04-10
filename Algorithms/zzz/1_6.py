def function(a, b, c):
    import math
    discr = b ** 2 - 4 * a * c

    if discr > 0:
        x1 = (-b + math.sqrt(discr)) / (2 * a)
        x2 = (-b - math.sqrt(discr)) / (2 * a)
        print(x1, x2)
    elif discr == 0:
        x = -b / (2 * a)
        print(x)
    else:
        print("Немає коренів")


a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

function(a, b, c)