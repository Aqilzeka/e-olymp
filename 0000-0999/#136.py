def nsd(x, y):
    while (x != 0) and (y != 0):
        if x > y:
            x = x % y
        else:
            y = y % x
    return x + y


temp = input().split()
x1, y1, x2, y2 = int(temp[0]), int(temp[1]), int(temp[2]), int(temp[3])
dx = abs(x2 - x1)
dy = abs(y2 - y1)
print(nsd(dx, dy) + 1)
